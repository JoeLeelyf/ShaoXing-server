from django.urls import path

from . import views

urlpatterns = [
    path('mainpage/swiperList', views.swiperList, name='swiperList'),
    path('mainpage/noticeList', views.getNoticeList, name='noticeList'),
    path('mainpage/gongxuList', views.gonxuList, name='gongxuList'),
    path('mainpage/centerList', views.centerList, name='centerList'),
    path('mainpage/contactway', views.contactway, name='contactway'),
    path('mainpage/excellentcompany',views.excellentcompany,name='excellentcompany'),
    path('mainpage/excellentperson',views.excellentperson,name='industry'),   
    path('mypage/ecard',view=views.getEcard,name='ecard'),
    path('mypage/privacy',view=views.getPrivacy,name='privacy'),
    path('mypage/authentication',view=views.getAuthentication,name='authentication'),
]