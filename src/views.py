from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def swiperList(request):
    res = {
        "message": [
        {
            "image_src": "https://static.botue.com/ugo/uploads/banner1.png"
        },
        {
            "image_src": "https://static.botue.com/ugo/uploads/banner2.png"
        },
        {
            "image_src": "https://static.botue.com/ugo/uploads/banner3.png"
        }
    ],
        "meta": {
                "msg":"获取成功",
                "status":200
        },
    }
    res= json.dumps(res)
    return HttpResponse(res)

def noticeList(request):
    res = {
        "message": [
        {
            "notice_id": 1,
            "notice_title": "英文简写",
            "notice_content": "balabala"
        },
        {
            "notice_id": 2,
            "notice_title": "英文简写",
            "notice_content": "balabala"
        },        {
            "notice_id": 3,
            "notice_title": "英文简写",
            "notice_content": "balabala"
        }
    ],
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
            "name-cn":"找政策",
            "name-en":"findPolicy",
            "image_src":"https://static.botue.com/ugo/uploads/icon_index_nav_4@2x.png",
        },
        {
            "name-cn":"找职业",
            "name-en":"findJob",
            "image_src":"https://static.botue.com/ugo/uploads/icon_index_nav_3@2x.png"
        },
        {
            "name-cn":"找人才",
            "name-en":"findPersonnel",
            "image_src":"https://static.botue.com/ugo/uploads/icon_index_nav_2@2x.png"
        },
        {
            "name-cn":"找技术",
            "name-en":"findTech",
            "image_src":"https://static.botue.com/ugo/uploads/icon_index_nav_1@2x.png"
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
            "name-cn":"站点地图",
            "name-en":"map",
            "image_src":"https://static.botue.com/ugo/uploads/icon_index_nav_4@2x.png",
        },
        {
            "name-cn":"站点查询",
            "name-en":"query",
            "image_src":"https://static.botue.com/ugo/uploads/icon_index_nav_3@2x.png"
        },
        {
            "name-cn":"预约服务",
            "name-en":"appointment",
            "image_src":"https://static.botue.com/ugo/uploads/icon_index_nav_2@2x.png"
        }
    ],
        "meta": {
                "msg":"获取成功",
                "status":200
        },
    }
    res= json.dumps(res)
    return HttpResponse(res)