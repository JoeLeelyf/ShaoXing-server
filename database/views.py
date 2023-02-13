from django.shortcuts import render
from django.http import HttpResponse

from .models import policy , career, tech

import json
# Create your views here.

def getPolicyList(request):
    last_policy_list = policy.objects.all().order_by('-time')[:10]
    mes_list=[]
    for i in last_policy_list:
        mes = {
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

def getCareerList(request):
    last_career_list = career.objects.all().order_by('-time')[:10]
    mes_list=[]
    for i in last_career_list:
        mes = {
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

def getTechList(request):
    last_tech_list = tech.objects.all().order_by('-time')[:10]
    mes_list=[]
    for i in last_tech_list:
        mes = {
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
