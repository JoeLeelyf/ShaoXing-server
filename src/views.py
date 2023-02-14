from django.shortcuts import render
from django.http import HttpResponse

from .models import notice

import json
# Create your views here.

def swiperList(request):
    res = {
        "message": [
        {
            "image_src": "https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/1155022637513865.jpg?sign=f849b0acc7f997a6e4542e6c888631fa&t=1676292062"
        },
        {
            "image_src": "https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/1155022637513865.jpg?sign=f849b0acc7f997a6e4542e6c888631fa&t=1676292062"
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
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E4%BC%81%E4%B8%9A.png?sign=4beef620d89a360be6d86d30654af02e&t=1676291609"
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
            "name_cn":"站点地图",
            "name_en":"map",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E5%9C%B0%E5%9B%BE%20(1).png?sign=eec13b41742089e5fffe686a40aa5ff4&t=1676291662",
        },
        {
            "name_cn":"站点查询",
            "name_en":"query",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E5%9C%B0%E5%9B%BE.png?sign=0a0a406ab76212a8ce6bc90586920b17&t=1676291678"
        },
        {
            "name_cn":"预约服务",
            "name_en":"appointment",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E9%A2%84%E7%BA%A6.png?sign=86ce3129b9aad624d1ab1b4dd4e5ed21&t=1676291692"
        }
    ],
        "meta": {
                "msg":"获取成功",
                "status":200
        },
    }
    res= json.dumps(res)
    return HttpResponse(res)