from django.urls import path 

from . import views

urlpatterns = [
    path('policy/list', views.getPolicyList, name='policyList'),
    path('policy/detail', views.getPolicyDetail, name='policyDetail'),
    path('career/list', views.getCareerList, name='careerList'),
    path('career/detail', views.getCareerDetail, name='careerDetail'),
    path('tech/list', views.getTechList, name='techList'),
    path('tech/detail', views.getTechDetail, name='techDetail'),
]