from django.urls import path

from . import models


urlpatterns = [
    path('baseInfo', models.User.getBaseInfo(), name='baseInfo'),
    path('detailInfo', models.User.getDetailInfo(), name='detailInfo'),
]