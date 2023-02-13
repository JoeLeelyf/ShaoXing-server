from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse
from django.shortcuts import render

import json, datetime
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=20,default="",blank=False,unique=True,verbose_name='姓名')
    phone = models.CharField(max_length=11,default="",blank=False,unique=True,verbose_name='手机号')
    email = models.EmailField(max_length=50,default="",blank=True,unique=True,verbose_name='邮箱')
    gender = models.CharField(max_length=10,default="",blank=True,verbose_name='性别')
    age = models.IntegerField(default=0,blank=True,verbose_name='年龄')
    hometown = models.CharField(max_length=20,default="",blank=True,verbose_name='籍贯')
    place = models.CharField(max_length=20,default="",blank=True,verbose_name='意向地点')
    trade = models.CharField(max_length=20,default="",blank=True,verbose_name='意向职业')
    position = models.CharField(max_length=20,default="",blank=True,verbose_name='意向岗位')
    salary = models.CharField(max_length=20,default="",blank=True,verbose_name='期望薪资')
    education = models.CharField(max_length=20,default="",blank=True,verbose_name='学历')
    school = models.CharField(max_length=20,default="",blank=True,verbose_name='毕业院校')
    positionaltitle = models.CharField(max_length=20,default="",blank=True,verbose_name='职称')
    countryposition = models.CharField(max_length=20,default="",blank=True,verbose_name='国家职业职称')
    field = models.CharField(max_length=20,default="",blank=True,verbose_name='专业领域')
    majorcate = models.CharField(max_length=20,default="",blank=True,verbose_name='专业大类')
    abroad = models.CharField(max_length=20,default="",blank=True,verbose_name='留学经历')
    experience = models.CharField(max_length=20,default="",blank=True,verbose_name='工作经历')
    experiences = models.CharField(max_length=20,default="",blank=True,verbose_name='工作经验')
    honors = models.CharField(max_length=20,default="",blank=True,verbose_name='业绩和荣誉')

    def __str__(self):
        return self.name
    
    def getBaseInfo(self):
        res = {
            "message":[
        {
            "name":"人才姓名",
            "manger": "专业",
            "education":"学历",
            "age":"年龄"
        }
        ],
        "meta":{
            "msg":"获取成功",
            "status":200
        }
        }
        res = json.dumps(res)
        return HttpResponse(res)
    
    def getDetailInfo(self):
        res = {
        "message":{
            "basicinfo":{
                "name":"人才姓名",
                "gender":"性别",
                "age":"年龄",
                "hometown":"籍贯",
            },
            "searchjobinfo":{
                "place":"意向地点",
                "trade":"意向行业",
                "position":"意向职位",
                "salary":"期望薪资"
            },
            "academicinfo":{
                "education":"学历",
                "school":"毕业院校",
                "positionaltitle":"职称",
                "countryposition":"国家职业资格",
                "field":"专业领域",
                "majorcate":"专业大类",
                "abroad":"留学经历"
            },
            "jobinfo":{
                "experience":"工作经验",
                "experiences":"工作经历",
                "honors":"业绩和荣誉"
            }
        },
        "meta":{
            "msg":"获取成功",
            "status":200
        }
}