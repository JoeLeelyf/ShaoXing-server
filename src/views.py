from django.shortcuts import render
from django.http import HttpResponse

from .models import notice, ecard, company, person, government, governmentContact
from ShaoXing.settings import BASE_DIR
from database.models import wxUser
import qrcode

import json
# Create your views here.

def swiperList(request):
    res = {
        "message": [
        {
            "image_src": "https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/WechatIMG2.jpeg?sign=6a3a62f58e3d8b8f7ab8705170656a0d&t=1676559401"
        },
        {
            "image_src": "https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/b693-hicsiav7327858.jpg?sign=8df9a9623dc8af7738bbf765b7ef706d&t=1676559381"
        },
        {
            "image_src": "https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/1155022637513865.jpg?sign=f849b0acc7f997a6e4542e6c888631fa&t=1676292062"
        }
    ],
        "meta": {
                "msg":"获取成功",
                "status":200
        },
    }
    res= json.dumps(res)
    return HttpResponse(res)

def getNoticeList(request):
    last_notice_list = notice.objects.all().order_by('-id')[:3]
    mes_list=[]
    for i in last_notice_list:
        mes = {
            "notice_id":i.id,
            "notice_title":i.title,
            "notice_content":i.content
        }
        mes_list.append(mes)
    res = {
        "message": mes_list,
        "meta": {
                "msg":"获取成功",
                "status":200
        },
    }
    res= json.dumps(res)
    return HttpResponse(res)

def gonxuList(request):
    res = {
        "message":[
        {
            "name_cn":"找政策",
            "name_en":"findpolicy",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E6%94%BF%E7%AD%96.png?sign=d84ea4024b51a26791e3105e9f46bb1f&t=1676291583",
        },
        {
            "name_cn":"找职业",
            "name_en":"findjob",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E5%85%AC%E6%96%87%E5%8C%85.png?sign=b124c3adbd2b6d606af32db4e28bf057&t=1676558951"
        },
        {
            "name_cn":"找人才",
            "name_en":"findpersonnel",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E4%BA%BA%E6%89%8D%E6%B5%81%E5%8A%A8%E3%80%81%E4%BA%BA%E6%89%8D%E5%87%BA%E5%85%A5%E5%A2%83.png?sign=53655de35dcad48515981ecc35f2a1b7&t=1676291625"
        },
        {
            "name_cn":"找技术",
            "name_en":"findtech",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E6%8A%80%E6%9C%AF%E6%9C%8D%E5%8A%A1.png?sign=91c3bcaec9a52cbd03dbf3eb1ec5558f&t=1676291650"
        }
    ],
        "meta": {
                "msg":"获取成功",
                "status":200
        },
    }
    res= json.dumps(res)
    return HttpResponse(res)

def centerList(request):
    res = {
        "message":[
        {
            "name_cn":"联系方式",
            "name_en":"contactway",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E9%A2%84%E7%BA%A6.png?sign=86ce3129b9aad624d1ab1b4dd4e5ed21&t=1676291692",
        },
        {
            "name_cn":"龙头企业",
            "name_en":"excellentcompany",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E4%BC%81%E4%B8%9A.png?sign=4beef620d89a360be6d86d30654af02e&t=1676291609"
        },
        {
            "name_cn":"名士通鉴",
            "name_en":"excellentperson",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E6%89%BE%E4%BA%BA%E6%89%8D.png?sign=55d933ff2902e371a2ba266582c566a6&t=1676558887"
        }
    ],
        "meta": {
                "msg":"获取成功",
                "status":200
        },
    }
    res= json.dumps(res)
    return HttpResponse(res)

def getEcard(request):
    baseUrl = "https://django-59g2-28953-7-1308482024.sh.run.tcloudbase.com/"
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
    user = wxUser.objects.all().get(phone=_phone)
    print(user)
    if user.level!="1" and user.level!="2" and user.level!="3":
        res = {
            "message":{
                "level":user.level,
            },
            "meta":{
                "msg":"您无法使用此功能",
                "status":200
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    else:
        if ecard.objects.filter(ownerid=user.id).exists():
            _ecard = ecard.objects.all().get(ownerid=user.id)
        else:
            info = "姓名："+user.name+"级别："+user.level+"电话："+user.phone
            img = qrcode.make(info)
            img.save(str(BASE_DIR) + ("/static/qrphoto/"+str(user.id)+".png"))
            _ecard = ecard.objects.create(ownerid=user.id, imgpath=baseUrl+"/static/qrphoto/"+str(user.id)+".png")
            _ecard.save()
        res = {
            "message":{
                "level":user.level,
                "imgurl":_ecard.imgpath
            },
            "meta":{
                "msg":"获取成功",
                "status":200
            }
        }
        return HttpResponse(json.dumps(res, default=str))

def contactway(request):
    if request.method!='GET':
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    mes_list = []
    for i in government.objects.all():
        phoneList = []
        emailList = []
        for j in governmentContact.objects.all().filter(governmentid=i.id):
            if j.contacttype=="phone":
                phoneList.append(str(j.contactor)+"："+str(j.contact))
            else:
                emailList.append(str(j.contactor)+"："+str(j.contact))
        mes_list.append({
            "government":i.name,
            "phone":phoneList,
            "email":emailList,
        }) 
    res = {
        "message":mes_list,
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    return HttpResponse(json.dumps(res, default=str))

def excellentcompany(request):
    if request.method!='GET':
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    mes_list = []
    for i in company.objects.all():
        mes_list.append({
            "name":i.name,
            "time":i.time,
            "master":i.master,
            "address":i.address,
            "phone":i.phone,
            "website":i.website,
            "email":i.email,
            "introduce":i.introduce,
            "photo":i.photo,
            "project":i.project,
        })
    res = {
        "message":mes_list,
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    return HttpResponse(json.dumps(res, default=str))

def excellentperson(request):
    if request.method!='GET':
        res = {
            "meta":{
                "msg":"Wrong request method!",
                "status":405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    mes_list = []
    for i in person.objects.all():
        mes_list.append({
            "name":i.name,
            "unique":i.unique,
            "photo":i.photo,
            "introduce":i.introduce,
        })
    res = {
        "message":mes_list,
        "meta":{
            "msg":"获取成功",
            "status":200
        }
    }
    return HttpResponse(json.dumps(res, default=str))



def getPrivacy(request):
    detail = "隐私政策\n "
    detail += "1. 本隐私政策适用于本应用程序（以下简称“本应用”）。\n"
    detail += "2. 本应用程序不会收集您的任何个人信息，包括但不限于姓名、电话号码、电子邮件地址、身份证号码、银行卡号、微信号、QQ号、微博号、支付宝账号、微信支付账号、支付宝支付账号、银行卡号、银行卡密码、银行卡验证码、银行卡有效期、银行卡安全码、银行卡绑定手机号码、银行卡绑定邮箱、银行卡绑定微信号、银行卡绑定QQ号、银行卡绑定微博号、银行卡绑定支付宝账号、银行卡绑定微信支付账号、银行卡绑定支付宝支付账号、银行卡绑定银行卡号、银行卡绑定银行卡密码、银行卡绑定银行卡验证码、银行卡绑定银行卡有效期、银行卡绑定银行卡安全码、银行卡绑定银行卡绑定手机号码、银行卡绑定银行卡绑定邮箱、银行卡绑定银行卡绑定微信号、银行卡绑定银行卡绑定QQ号、银行卡绑定银行卡绑定微博号、银行卡绑定银行卡绑定支付宝账号、银行卡绑定银行卡绑定微信支付账号、银行卡绑定银行卡绑定支付宝支付账号、银行卡绑定银行卡绑定银行卡号、银行卡绑定银"
    detail += "行卡绑定银行卡密码、银行卡绑定银行卡绑定银行卡验证码"
    return HttpResponse(detail)


