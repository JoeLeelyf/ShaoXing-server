from django.urls import path

from . import views

urlpatterns = [
    path('mainpage/swiperList', views.swiperList, name='swiperList'),
    path('mainpage/noticeList', views.noticeList, name='noticeList'),
    path('mainpage/gongxuList', views.gonxuList, name='gongxuList'),
    path('mainpage/centerList', views.centerList, name='centerList'),
]