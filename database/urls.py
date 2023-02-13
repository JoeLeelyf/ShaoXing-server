from django.urls import path 

from . import views

urlpatterns = [
    path('police/list', views.getPoliceList, name='policeList'),
    path('police/detail', views.getPoliceDetail, name='policeDetail'),
    path('career/list', views.getCareerList, name='careerList'),
    path('career/detail', views.getCareerDetail, name='careerDetail'),
]