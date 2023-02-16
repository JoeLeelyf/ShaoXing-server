from django.db import models
import datetime

# Create your models here.
class policy(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.datetime.now)
    unit = models.CharField(max_length=255)
    content = models.TextField()
    class Meta:
        db_table = 'police'
    
    def __str__(self):
        return self.title

class career(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.datetime.now)
    unit = models.CharField(max_length=255)
    content = models.TextField()
    salary = models.CharField(max_length=255)
    jobinfo = models.CharField(max_length=255)
    contactor = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,blank=True)
    companyname = models.CharField(max_length=255)
    companyinfo = models.CharField(max_length=255)
    class Meta:
        db_table = 'career'
    
    def __str__(self):
        return self.title

class tech(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(max_length=255)
    class Meta:
        db_table = 'tech'
    
    def __str__(self):
        return self.title

class wxUser(models.Model):
    id = models.AutoField(primary_key=True)
    avatarUrl = models.URLField(max_length=255)
    phone = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=30, blank=False)
    nickname = models.CharField(max_length=30, blank=True)
    level = models.CharField(max_length=1,choices=((1,'A'),(2,'B'),(3,'C'),(4,'D'),(5,'E'),(6,'F')))
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
    abroad = models.CharField(max_length=30, blank=True)
    experience = models.CharField(max_length=30, blank=True)
    experiences = models.CharField(max_length=30, blank=True)
    honors = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = 'wxUser'

    def __str__(self):
        return self.name
    
    
class comment(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default=-1,choices=((-1,'comment'),(0,'policy'),(1,'job')))
    foreignid = models.IntegerField() # comment for which id, whether policy, job or another comment
    commenterid = models.IntegerField() # wxUser who made this comment
    time = models.DateTimeField(default=datetime.datetime.now)
    content = models.TextField()

    class Meta:
        db_table = 'comment'
    
    def __str__(self):
        return self.content