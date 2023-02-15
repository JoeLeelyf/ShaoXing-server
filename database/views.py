from django.shortcuts import render
from django.http import HttpResponse

from .models import policy , career, tech
from WXUser.models import Profile

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
    if requst.method == 'POST':
        rec = json.loads(requst.body)
        _id = int(rec['id'])
    else:
        return HttpResponse("Wrong request method!")
    policy_detail = policy.objects.get(id=_id)
    policy_title = policy_detail.title
    policy_content = policy_detail.content
    res = {
        "message":{
            "title":policy_title,
            "content":policy_content
        },
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
    if request.method == 'POST':
        rec = json.loads(request.body)
        _id = int(rec['id'])
    else:
        return HttpResponse("Wrong request method!")
    career_detail = career.objects.get(id=_id)
    career_title = career_detail.title
    career_salary = career_detail.salary
    career_jobinfo = career_detail.jobinfo
    career_contactor = career_detail.contactor
    career_phone = career_detail.phone
    career_email = career_detail.email
    career_companyname = career_detail.companyname
    career_companyinfo = career_detail.companyinfo
    res = {
        "message":{
            "title":career_title,
            "salary":career_salary,
            "jobinfo":career_jobinfo,
            "contactinfo":{
                "contactor":career_contactor,
                "phone":career_phone,
                "email":career_email
            },
            "companydetail":{
                "companyname":career_companyname,
                "companyinfo":career_companyinfo
            }
        },
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
    if request.method == 'POST':
        rec = json.loads(request.body)
        _id = int(rec['id'])
    else:
        return HttpResponse("Wrong request method!")
    tech_detail = tech.objects.get(id=_id)
    tech_title = tech_detail.title
    tech_field = tech_detail.field
    tech_level = tech_detail.level
    tech_time = tech_detail.time
    tech_status = tech_detail.status
    res = {
        "message":{
            
        },
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)


# ========================================================
def getPersonnelList(request):
    if request.method == 'POST':
        rec = json.loads(request.body)
        _page = int(rec['_page'])
        _pageSize = int(rec['_pageSize'])
    else:
        return HttpResponse("Wrong request method!")
    last_personnel_list = Profile.objects.all.order_by('-age')
    mes_list=[]
    for i in last_personnel_list:
        mes = {
            
        }

def getPersonnelDetail(request):
    if request.method == 'POST':
        rec = json.loads(request.body)
    else:
        return HttpResponse('Wrong request method!')
    