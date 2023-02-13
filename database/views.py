from django.shortcuts import render
from django.http import HttpResponse

from .models import police , career

import json
# Create your views here.

def getPoliceList(request):
    last_police_list = police.objects.all().order_by('-time')[:10]
    mes_list=[]
    for i in last_police_list:
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

def getPoliceDetail(requst):
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