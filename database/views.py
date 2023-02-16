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
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
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
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
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
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
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
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
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
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
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
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    tech_detail = tech.objects.get(id=_id)
    tech_title = tech_detail.title
    tech_field = tech_detail.field
    tech_level = tech_detail.level
    tech_time = tech_detail.time
    tech_status = tech_detail.status
    res = {
        "message":{
            "title":tech_title,
            "field":tech_field,
            "level":tech_level,
            "time":tech_time,
            "status":tech_status
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
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
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
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
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
def getCommentList(_status,_id):
    comment_father_list = []
    comment_father_list = comment.objects.filter(status=_status).filter(foreignid=_id).order_by('-time')
    comment_list = []
    # comment in this list, which status is 0 or 1
    for i in comment_father_list:
        comment_list.append(i)
        comment_list+=comment.objects.filter(status=-1).filter(foreignid=i.id).order_by('-time')
    mes_list = []
    for i in comment_list:
        commenter = wxUser.objects.all().get(id=i.commenterid)
        mes = {
            "status": i.status,
            "commenterid": i.commenterid,
            "avatar": commenter.avatarUrl,
            "nickname": commenter.nickname,
            "replyNickname": commenter.nickname,
            "createTime": i.time,
            "content": i.content
        }
        mes_list.append(mes)
    return mes_list

def getPolicyCommentList(request):
    if request.method == 'POST':
        rec = json.loads(request.body)
        _id = int(rec['id'])
    else:
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    mes_list = getCommentList(0,_id)
    res = {
        "message":mes_list,
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
    comment_list = getCommentList(1,_id)
    res = {
        "message":comment_list,
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)

def updateComment(request,isPolicy:bool):
    if request.method == 'POST':
        rec = json.loads(request.body)
        status = int(rec['status'])
        commenterphoneid = int(rec['phoneid'])
        time = rec['time']
        foreignid = int(rec['preuser'])
        content = rec['content']
    else:
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))

    if status == 1:
        status = -1
    elif isPolicy and status == 0:
        status = 0
    elif not isPolicy and status == 0:
        status = 1
    else:
        return HttpResponse("ERROR!")
    commenterid = comment.objects.all().get(phone=commenterphoneid)
    new_comment = comment(status=status, commenterid=commenterid, time=time, foreignid=foreignid, content=content)
    new_comment.save()
    res = {
        "meta":{
            "msg":"评论成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)

def updatePolicyComment(request):
    return updateComment(request, True)

def updateJobComment(request):
    return updateComment(request, False)


# ========================================================
def signup(request):
    try:
        if request.method == 'POST':
            rec = json.loads(request.body)
            _avatarUrl = rec['avatar']
            _nickname = rec['nickname']
            _phone = rec['phone']
            _password = rec['password']
        else:
            res = {
                "meta":{
                    "msg":"Wrong request method!",
                    "status":405
                }
            }
            return HttpResponse(json.dumps(res, default=str))
    except Exception as e:
        res = {
            "meta":{
                "msg":"Wrong request body!",
                "status":400
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    if wxUser.objects.all().filter(phone=_phone).count()!=0:
        res = {
            "meta":{
                "msg":"用户已存在",
                "status":401
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    new_wxUser = wxUser(phone=_phone, password=_password, avatarUrl=_avatarUrl, nickname=_nickname, name = _nickname)
    new_wxUser.save()
    res = {
        "meta":{
            "msg":"注册成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)
        

def login(request):
    try:
        if request.method == 'POST':
            rec = json.loads(request.body)
            _phone = rec['phone']
            _password = rec['password']
        else:
            return HttpResponse('ERROR!')
    except Exception as e:
        return HttpResponse(e)
    user = wxUser.objects.all().filter(phone=_phone)
    if user.count() == 0:
        res = {
            "meta":{
                "msg":"用户不存在",
                "status":401.1
            }
        }
    elif str(user[0].password) != str(_password):
        res = {
            "meta":{
                "msg":"密码错误",
                "status":401.1
            }
        }
    else:
        res = {
            "meta":{
                "msg":"登录成功",
                "status":200
            }
        }
    res = json.dumps(res)
    return HttpResponse(res)