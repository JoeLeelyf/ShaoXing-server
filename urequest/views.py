from django.shortcuts import render
from django.http import HttpResponse
from .models import authentication , jobexperience, eduexperience, persontype
import json

# Create your views here.
def requestAuthentication(request):
    if request.method != 'POST':
        res = {
            "message": "请求方式错误",
            "meta": {
                "msg":"请求方式错误",
                "status": 405
            }
        }
        return HttpResponse(json.dumps(res, default=str))
    rec = json.loads(request.body)
    _name = rec['name']
    _country = rec['country']
    _gender = rec['gender']
    _phone = rec['phone']
    _cardtype = rec['cardtype']
    _cardnum = rec['cardnum']
    _currentunit = rec['currentunit']
    _jobexperience = rec['jobexperience']
    _eduexperience = rec['eduexperience']
    _persontype = rec['persontype']
    new_auth=authentication.objects.all().create(name=_name, country=_country, gender=_gender, phone=_phone, cardtype=_cardtype, cardnum=_cardnum, currentunit=_currentunit, persontype=_persontype)
    new_auth.save()
    for i in _jobexperience:
        new_job=jobexperience.objects.create(unitname=i['unitname'], unitaddress=i['unitaddress'], starttime=i['starttime'], endtime=i['endtime'], field=i['field'], typeJobExp=i['type'], auth=new_auth)
        new_job.save()

    for i in _eduexperience:
        new_edu=eduexperience.objects.create(school=i['school'], edulevel=i['edulevel'], starttime=i['starttime'], endtime=i['endtime'], major=i['major'], auth=new_auth)
        new_edu.save()
    
    for i in _persontype:
        new_persontype=persontype.objects.create(type=i['type'], time=i['time'], auth=new_auth)
        new_persontype.save()
    res = {
        "message": "请求成功",
        "meta": {
            "msg":"请求成功",
            "status": 200
        }
    }
    return HttpResponse(json.dumps(res, default=str))