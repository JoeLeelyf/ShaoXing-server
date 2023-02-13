from django.shortcuts import render
from django.http import HttpResponse
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
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E6%94%BF%E7%AD%96.png?sign=d84ea4024b51a26791e3105e9f46bb1f&t=1676291583",
        },
        {
            "name-cn":"找职业",
            "name-en":"findJob",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E4%BC%81%E4%B8%9A.png?sign=4beef620d89a360be6d86d30654af02e&t=1676291609"
        },
        {
            "name-cn":"找人才",
            "name-en":"findPersonnel",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E4%BA%BA%E6%89%8D%E6%B5%81%E5%8A%A8%E3%80%81%E4%BA%BA%E6%89%8D%E5%87%BA%E5%85%A5%E5%A2%83.png?sign=53655de35dcad48515981ecc35f2a1b7&t=1676291625"
        },
        {
            "name-cn":"找技术",
            "name-en":"findTech",
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
            "name-cn":"站点地图",
            "name-en":"map",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E5%9C%B0%E5%9B%BE%20(1).png?sign=eec13b41742089e5fffe686a40aa5ff4&t=1676291662",
        },
        {
            "name-cn":"站点查询",
            "name-en":"query",
            "image_src":"https://prod-6g0a1d1h5dcb92d9-1308482024.tcloudbaseapp.com/icon/%E5%9C%B0%E5%9B%BE.png?sign=0a0a406ab76212a8ce6bc90586920b17&t=1676291678"
        },
        {
            "name-cn":"预约服务",
            "name-en":"appointment",
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