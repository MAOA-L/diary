from django.db.models import Count
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import random
import hashlib
from .models import Log, AdminDiary
from app_upload.models import Article, Sort
from collections import defaultdict
from diary import globalContext
import copy
import jieba
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def logging(func):
    def wraper(request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        log = Log()
        try:
            username = request.META.get('USERNAME')
            path = request.path
            log.ip = ip
            log.name = username
            log.url = path
            log.save()
        except:
            log.ip = 'wrong'
            log.name = 'wrong'
            log.url = 'wrong'
            log.save()

        return func(request)
    return wraper


def jurisdiction(func):
    """权限过滤，用于分享权限过滤"""
    def wraper(request, dia):
        try:
            a = AdminDiary.objects.get(identification_id=dia)
            session = request.session['share_password'] if 'share_password' in request.session else ''
            print('session==', session)
            if a.share or session == '1996Chan':
                return func(request, dia)
            else:
                context = {'title': 'No Power', 'content': 'You Have No Power To have This Text', 'next': dia}
                return render(request, 'jurisdiction_show.html', context)
        except:
            context = {'title': 'accident', 'content': 'an accident was happend OR you have no power hahahaha', 'next': dia}
            return render(request, 'jurisdiction_show.html', context)

    return wraper


def add_power(request):
    next = request.GET.get('next')
    print('next=', next)
    if request.method == 'POST':
        password = request.POST['share_password']
        print('password', password)
        if password == '1996Chan':
            request.session['share_password'] = password
            request.session.set_expiry(0)
            return HttpResponseRedirect('detail/'+next)
        else:
            context = {'title': 'accident', 'content': 'an accident was happend!'}
            return render(request, 'jurisdiction_show.html', context)


def index(request, page=1):
    page = 1 if page == 0 else page
    article_list = Article.objects.all().select_related().order_by('-gmt_create')
    p = []
    for i in article_list:
        p.append(i)
    paginator = Paginator(article_list, 1)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    print(p.number)
    g = copy.deepcopy(globalContext.primary())
    g['home']['active'] = 'menu-item-active'
    g['articleList'] = p
    return render(request, 'index.html', g)


# @jurisdiction
def detail(request, uuid):
    article = Article.objects.get(uuid=uuid)
    return render(request, 'detail.html', {"article": article})


def search(request):
    p = copy.deepcopy(globalContext.primary())
    p['search']['active'] = 'menu-item-active'
    return render(request, 'search.html', {})


def search_result(request, art):
    words = jieba.cut(art, cut_all=False)
    # 获取数据
    result = []
    for w in words:
        if w == '' or w is None:
            continue
        result.append([w for w in Article.objects.values("uuid", "title").filter(title__contains=w)])

    return HttpResponse(json.dumps(result))


def archive(request):
    """
    归档页面
    :param request:
    :return:
    """
    p = copy.deepcopy(globalContext.primary())
    p['archive']['active'] = 'menu-item-active'
    # 获取所有文档的标题与时间
    article = Article.objects.all().values('uuid', 'gmt_create', 'title')
    # 统计所有文章数
    article_count = Article.objects.count()
    article_list = defaultdict(list)
    for i in article:
        i['time'] = i['gmt_create'].strftime('%m-%d')
        article_list[i['gmt_create'].strftime("%Y")].append(i)
    p['archive']['article'] = dict(article_list)
    p['archive']['count'] = article_count
    return render(request, "archive.html", p)


def categories(request):
    """分类页面"""
    p = copy.deepcopy(globalContext.primary())
    p['categories']['active'] = 'menu-item-active'
    # 获取分类信息
    a = Article.objects.values("sort").annotate(count=Count('sort'))
    p['categories']['data'] = [w for w in a]
    p['categories']['count'] = Article.objects.values('sort').distinct().count()
    return render(request, "categorie.html", p)


def categories_list(request, name):
    """具体分类列表页面"""
    print(name)
    p = copy.deepcopy(globalContext.primary())
    p['categories']['active'] = 'menu-item-active'
    p['categories']['sortName'] = name
    p['categories']['article'] = Article.objects.filter(sort=name)

    return render(request, "categorie_list.html", p)


def timeline(request):
    p = copy.deepcopy(globalContext.primary())
    p['version']['active'] = 'menu-item-active'
    return render(request, "version_develop.html", p)
