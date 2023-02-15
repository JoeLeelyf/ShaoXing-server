from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def empty_items():
    return {'items': []}

class Profile(models.Model):
    # 与User外键连接
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 用户数据
    name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    age = models.IntegerField(blank=True, null=True)
    hometown = models.CharField(max_length=30, blank=True)
    place = models.CharField(max_length=30, blank=True)
    trade = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=30, blank=True)
    salary = models.CharField(max_length=30, blank=True)
    education = models.CharField(max_length=30, blank=True)
    school = models.CharField(max_length=30, blank=True)
    positionaltitle = models.CharField(max_length=30, blank=True)
    countryposition = models.CharField(max_length=30, blank=True)
    field = models.CharField(max_length=30, blank=True)
    majorate = models.CharField(max_length=30, blank=True)
    aboard = models.CharField(max_length=30, blank=True)
    experience = models.CharField(max_length=30, blank=True)
    experiences = models.CharField(max_length=30, blank=True)
    honors = models.CharField(max_length=30, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()