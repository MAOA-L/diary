from django.test import TestCase
import requests

url = "http://10.70.3.104/xgxt/xsxx_xsgl.do"
# headers = {
#     'Cookie': 'JSESSIONID=280FA7D9F16904D543BB4C7F855A595C'
# }
headers = {
    'Cookie': 'JSESSIONID=C4FA8E7D02023931F71A1CAC8C19FD66'
}
data = {
    'method': 'showPhoto',
    'xh': 2015014148
}
for i in range(2015014148, 2015014149):
    data['xh'] = i
    p = requests.post(url, headers=headers, data=data, timeout=3)
    print(p.url)
    with open("C:/Users/10993/Desktop/img/{}".format(i)+".jpg", "wb") as f:
        f.write(p.content)



