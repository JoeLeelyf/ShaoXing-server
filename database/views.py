from django.shortcuts import render
from django.http import HttpResponse

from .models import policy , career, tech, wxUser, comment

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
    last_personnel_list = wxUser.objects.all().order_by('-id')[(_page-1)*_pageSize:_page*_pageSize]
    mes_list=[]
    for i in last_personnel_list:
        mes = {
            "id":i.id,
            "name":i.name,
            "manger":i.majorate,
            "education":i.education,
            "age":i.age
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

def getPersonnelDetail(request):
    if request.method == 'POST':
        rec = json.loads(request.body)
        _id = int(rec['id'])
    else:
        return HttpResponse('Wrong request method!')
    personnel_detail = wxUser.objects.get(id=_id)
    personnel_name = personnel_detail.name
    personnel_gender = personnel_detail.gender
    personnel_age = personnel_detail.age
    personnel_hometown = personnel_detail.hometown
    personnel_place = personnel_detail.place
    personnel_trade = personnel_detail.trade
    personnel_position = personnel_detail.position
    personnel_salary = personnel_detail.salary
    personnel_education = personnel_detail.education
    personnel_school = personnel_detail.school
    personnel_positionaltitle = personnel_detail.positionaltitle
    personnel_countryposition = personnel_detail.countryposition
    personnel_field = personnel_detail.field
    personnel_majorcate = personnel_detail.majorate
    personnel_abroad = personnel_detail.abroad
    personnel_experience = personnel_detail.experience
    personnel_experiences = personnel_detail.experiences
    personnel_honors = personnel_detail.honors
    res = {
        "message":{
            "id": _id,
            "basicinfo":{
                "name":personnel_name,
                "gender":personnel_gender,
                "age":personnel_age,
                "hometown":personnel_hometown,
            },
            "searchjobinfo":{
                "place":personnel_place,
                "trade":personnel_trade,
                "position":personnel_position,
                "salary":personnel_salary
            },
            "academicinfo":{
                "education":personnel_education,
                "school":personnel_school,
                "positionaltitle":personnel_positionaltitle,
                "countryposition":personnel_countryposition,
                "field":personnel_field,
                "majorcate":personnel_majorcate,
                "abroad":personnel_abroad
            },
            "jobinfo":{
                "experience":personnel_experience,
                "experiences":personnel_experiences,
                "honors":personnel_honors
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
def getCommentList(status):
    pass

def getPolicyCommentList(request):
    if request.method == 'POST':
        rec = json.loads(request.body)
        _id = int(rec['id'])
    else:
        return HttpResponse("Wrong request method!")
    comment_list = getCommentList(0)
    res = {
        "message":comment_list,
        "meta":{
        "msg":"获取成功",
        "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)

def getJobCommentList(request):
    if request.method == 'POST':
        rec = json.loads(request.body)
        _id = int(rec['id'])
    else:
        return HttpResponse("Wrong request method!")
    comment_list = getCommentList(1)
    res = {
        "message":comment_list,
        "meta":{
        "msg":"获取成功",
        "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)

def updatePolicyComment(request):
    pass

def updateJobComment(request):
    pass