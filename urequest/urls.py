from django.urls import path 

from . import views

urlpatterns = [
    path('requestAuthentication', views.requestAuthentication, name='requestAuthentication'),
]