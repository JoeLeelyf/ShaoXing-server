from django.shortcuts import render
from django.http import HttpResponse

from .models import policy , career, tech, wxUser, comment

import json
# Create your views here.

# Policy
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

# Job/Career
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

# Tech
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
    tech_stage = tech_detail.stage
    tech_introduction = tech_detail.introduce
    tech_type = tech_detail.typeTech
    tech_master = tech_detail.master
    tech_phone = tech_detail.phone
    tech_email = tech_detail.email
    res = {
        "message":{
            "title":tech_title,
            "field":tech_field,
            "level":tech_level,
            "time":tech_time,
            "status":tech_status,
            "stage":tech_stage,
            "introduce":tech_introduction,
            "type":tech_type,
            "master":tech_master,
            "phone":tech_phone,
            "email":tech_email
        },
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    res = json.dumps(res, default=str)
    return HttpResponse(res)

# Personnel
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
            "phone":i.phone,
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
        _phone = rec['phone']
    else:
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    try:
        personnel_detail = wxUser.objects.get(phone=_phone)
    except Exception as e:
        res = {
            "meta":{
                "msg":str(e),
                "status":400
            }
        }
        return HttpResponse(json.dumps(res))
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
            "phone": _phone,
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
    
# Comment
# ========================================================
def getCommentList(_status,_id):
    comment_father_list = [] 
    comment_father_list = comment.objects.filter(status=_status).filter(preid=_id).order_by('-time')
    comment_list = []
    # comment in this list, which status is 0 or 1
    for i in comment_father_list:
        comment_list.append(i)
        comment_list+=comment.objects.filter(status=-1).filter(preid=i.id).order_by('-time')
    mes_list = []
    if i.status == 0 or i.status == 1:
        status_ret=0
    else:
        status_ret=1
    for i in comment_list:
        commenter = wxUser.objects.all().get(id=i.commenterid)
        mes = {
            "id": i.id,
            "status": status_ret,
            "commenterid": commenter.phone,
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
        commenterphoneid = rec['phoneid']
        time = rec['time']
        preid = rec['preuser'] 
        content = rec['content']
        superid = int(rec['superid'])
    else:
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))

    if status == 1: # preid is the id of the pre comment
        status = -1
        comment.objects.all().get(id=preid).isReply = True

    elif isPolicy and status == 0:
        status = 0
    elif not isPolicy and status == 0:
        status = 1
    else:
        return HttpResponse("ERROR!")
    preid = int(preid)

    commenter = wxUser.objects.all().get(phone=commenterphoneid)
    new_comment = comment(status=status, superid=superid,commenterid=commenter.id, time=time, preid=preid, content=content)
    new_comment.save()
    if isPolicy:
        new_comment.supertype = "policy"
    else:
        new_comment.supertype = "job"
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

# User
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
    user = wxUser.objects.all().filter(phone=_phone)
    if user.count() == 0:
        res = {
            "meta":{
                "msg":"用户不存在",
                "status":401.1
            }
        }
        return HttpResponse(json.dumps(res))
    user = wxUser.objects.all().get(phone=_phone)
    if str(user.password)!= str(_password):
        res = {
            "meta":{
                "msg":"密码错误",
                "status":401.1
            }
        }
    else:
        res = {
            "message":{
                "avatar":user.avatarUrl,
                "nickname":user.nickname
            },
            "meta":{
                "msg":"登录成功",
                "status":200
            }
        }
    res = json.dumps(res)
    return HttpResponse(res)

def editProfile(request):
    try:
        if request.method == 'POST':
            rec = json.loads(request.body)
            _phone = rec['phone']
            _name = rec['name']
            _gender = rec['gender']
            _age = rec['age']
            _hometown = rec['hometown']
            _place = rec['place']
            _trade = rec['trade']
            _position = rec['position']
            _salary = rec['salary']
            _education = rec['education']
            _school = rec['school']
            _positionaltitle = rec['positionaltitle']
            _countryposition = rec['countryposition']
            _field = rec['field']
            _majorate = rec['majorate']
            _abroad = rec['abroad']
            _experience = rec['experience']
            _experiences = rec['experiences']
            _honors = rec['honors']
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
    user = wxUser.objects.all().filter(phone=_phone)
    if user.count() == 0:
        res = {
            "meta":{
                "msg":"用户不存在",
                "status":401.1
            }
        }
        return HttpResponse(json.dumps(res))
    try:
        user = wxUser.objects.all().get(phone=_phone)
        if _name!="":
            user.name = _name
        if  _gender!="":
            user.gender = _gender
        if _age!="":
            user.age = int(_age)
        if _hometown!="":
            user.hometown = _hometown
        if _place!="":
            user.place = _place
        if _trade!="":
            user.trade = _trade
        if _position!="":
            user.position = _position
        if _salary!="":
            user.salary = _salary
        if _education!="":
            user.education = _education
        if _school!="":
            user.school = _school
        if _positionaltitle!="":
            user.positionaltitle = _positionaltitle
        if _countryposition!="":
            user.countryposition = _countryposition
        if _field!="":
            user.field = _field
        if _majorate!="":
            user.majorate = _majorate
        if _abroad!="":
            user.abroad = _abroad
        if _experience!="":
            user.experience = _experience
        if _experiences!="":
            user.experiences = _experiences
        if _honors!="":
            user.honors = _honors
        user.save()
        res = {
            "meta":{
                "msg":"修改简历成功",
                "status":200
            }
        }
        return HttpResponse(json.dumps(res))
    except Exception as e:
        res = {
            "meta":{
                "msg":str(e),
                "status":400
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    

# Search
# ========================================================
def search(request):
    if request.method != 'POST':
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    rec = json.loads(request.body)
    _keyword = rec['keyword']
    _type = rec['type']

    mes_list = []
    if _type == 'home':
        mes_list = searchHome(_keyword)
    elif _type == 'policy':
        mes_list = searchPolicy(_keyword)
    elif _type == 'job':
        mes_list = searchJob(_keyword)
    elif _type == 'personnel':
        mes_list = searchPersonnel(_keyword)
    elif _type == 'tech':
        mes_list = searchTech(_keyword)
    else:
        res = {
            "meta":{
                "msg":"Wrong type!",
                "status":400
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    res = {
        "message":mes_list,
        "meta":{
            "msg":"搜索成功",
            "status":200
        }
    }
    return HttpResponse(json.dumps(res, default=str))

def searchPolicy(_keyword):
    mes_list = []
    policy_list = policy.objects.all().filter(title__contains=_keyword)
    for Policy in policy_list:
        mes = {
            "id":Policy.id,
            "title":Policy.title,
            "type":"policy"
        }
        mes_list.append(mes)
    return mes_list

def searchJob(_keyword):
    mes_list = []
    job_list = career.objects.all().filter(title__contains=_keyword)
    for Job in job_list:
        mes = {
            "id":Job.id,
            "title":Job.title,
            "type":"job"
        }
        mes_list.append(mes)
    return mes_list

def searchPersonnel(_keyword):
    mes_list = []
    personnel_list = wxUser.objects.all().filter(name__contains=_keyword)
    for Personnel in personnel_list:
        mes = {
            "id":Personnel.phone,
            "title":Personnel.name,
            "type":"personnel"
        }
        mes_list.append(mes)
    return mes_list

def searchTech(_keyword):
    mes_list = []
    tech_list = tech.objects.all().filter(title__contains=_keyword)
    for Tech in tech_list:
        mes = {
            "id":Tech.id,
            "title":Tech.title,
            "type":"tech"
        }
        mes_list.append(mes)
    return mes_list

def searchHome(_keyword):
    mes_list = []
    if searchJob(_keyword)!=[]:
        mes_list += searchJob(_keyword)
    if searchPersonnel(_keyword)!=[]:
        mes_list += searchPersonnel(_keyword)
    if searchPolicy(_keyword)!=[]:
        mes_list += searchPolicy(_keyword)
    if searchTech(_keyword)!=[]:
        mes_list += searchPolicy(_keyword)
    return mes_list


# CommentNotice
# ========================================================
def commentNotice(request):
    if request.method != 'POST':
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    rec = json.loads(request.body)
    _phone = rec['phone']
    _user_list = wxUser.objects.all().filter(phone=_phone)
    if _user_list.count() == 0:
        res = {
            "meta":{
                "msg":"用户不存在",
                "status":401.1
            }
        }
        return HttpResponse(json.dumps(res))
    _user = wxUser.objects.all().get(phone=_phone)
    _comment_list = comment.objects.all().filter(isReply=True,preid=_user.id)
    print(_comment_list)
    _comment_list = _comment_list.order_by('-time')
    res_list = []
    for _comment in _comment_list:
        _res = {
            "type":_comment.supertype,
            "articleid":_comment.superid,
            "nikename":_user.nickname,
            "time":_comment.time,
            "avatar":_user.avatarUrl,
            "content":_comment.content
        }
        res_list.append(_res)
    res = {
        "message":res_list,
        "meta":{
            "msg":"获取评论成功",
            "status":200
        }
    }
    return HttpResponse(json.dumps(res, default=str))
