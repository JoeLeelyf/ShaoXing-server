from django.shortcuts import render
from django.http import HttpResponse

from .models import policy , career, tech

import json
# Create your views here.

def getPolicyList(request):
    if request.method == 'POST':
        rec = json.loads(request.body)
        _page = int(rec['_page'])
        _pageSize = int(rec['_pageSize'])
    else:
        return HttpResponse("Wrong request method!")
    last_policy_list = policy.objects.all().order_by('-time')[(_page-1)*_pageSize:_page*_pageSize]
    mes_list=[]
    for i in last_policy_list:
        mes = {
            "id":i.id,
            "title":i.title,
            "time":i.time,
            "unit":i.unit
        }
        mes_list.append(mes)
    res = {
        "message":mes_list,
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)

def getPolicyDetail(requst):
    res = {
        "message":[

        ],
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)

# ========================================================

def getCareerList(request):
    if request.method == 'POST':
        rec = json.loads(request.body)
        _page = int(rec['_page'])
        _pageSize = int(rec['_pageSize'])
    else:
        return HttpResponse("Wrong request method!")
    last_career_list = career.objects.all().order_by('-time')[(_page-1)*_pageSize:_page*_pageSize]
    mes_list=[]
    for i in last_career_list:
        mes = {
            "id":i.id,
            "title":i.title,
            "time":i.time,
            "content":i.content
        }
        mes_list.append(mes)
    res = {
        "message":mes_list,
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)

def getCareerDetail(request):
    res = {
        "message":[

        ],
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)

# ========================================================

def getTechList(request):
    if request.method == 'POST':
        rec = json.loads(request.body)
        _page = int(rec['_page'])
        _pageSize = int(rec['_pageSize'])
    else:
        return HttpResponse("Wrong request method!")
    last_tech_list = tech.objects.all().order_by('-time')[(_page-1)*_pageSize:_page*_pageSize]
    mes_list=[]
    for i in last_tech_list:
        mes = {
            "id":i.id,
            "title":i.title,
            "field":i.field,
            "level":i.level,
            "time":i.time,
            "status":i.status
        }
        mes_list.append(mes)
    res = {
        "message":mes_list,
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)

def getTechDetail(request):
    res = {
        "message":[

        ],
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)
