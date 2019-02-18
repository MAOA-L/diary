from django.shortcuts import render, HttpResponseRedirect
from diary.globalContext import Primary
import requests, re, json


def qq_login(request):
    # 根据参数返回需要获取code的url
    # 根据回调过来的code获取access_token
    client_id = 101549521
    client_secret = "df357795e13de29dcd168354b34f0509"
    code = request.GET.get("code")
    redirect_uri = "http://mfweb.cyanzoy.top:8080/xadmin/qq_login"
    url = "https://graph.qq.com/oauth2.0/token?grant_type=authorization_code&client_id={}&client_secret={}&code={}&redirect_uri={}"
    p = requests.get(url=url.format(client_id, client_secret, code, redirect_uri)).content.decode("UTF-8")
    # 输出access_token等信息
    list_three = p.split("&")
    three_arg = {}
    for _ in list_three:
        three_arg[_.split("=")[0]] = _.split("=")[1]

    # 根据access_token获取openid
    clientid_openid = requests.get(url="https://graph.qq.com/oauth2.0/me?access_token={}".format(three_arg["access_token"])).content.decode("UTF-8")
    callback = re.match("callback\((.*)\)", clientid_openid).group(1)
    callback_json = json.loads(callback)
    openid = callback_json["openid"]
    # Access Token以及OpenID来访问用户信息->openid来识别用户
    user = requests.get("https://graph.qq.com/user/get_user_info?access_token={}&oauth_consumer_key={}&openid={}"
                        .format(three_arg["access_token"], client_id, openid)).content.decode("utf-8")
    print(json.loads(user)['figureurl'])

    return render(request, "statistic.html", {"username": json.loads(user)['nickname']})


def login(request):
    return render(request, "login.html", {})


def index(request):
    context = {
        "parent_id": Primary.global_context["xadmin"]["statistic"]["parent_id"] - 1,
        "current_id": Primary.global_context["xadmin"]["publish"]["current_id"] - 1,
    }
    return render(request, "statistic.html", context)


def publish(request):
    context = {
        "parent_id": Primary.global_context["xadmin"]["publish"]["parent_id"] - 1,
        "current_id": Primary.global_context["xadmin"]["publish"]["current_id"],
    }
    return render(request, "publish.html", context)
