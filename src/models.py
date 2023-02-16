from django.db import models
from database.models import wxUser
import datetime

# Create your models here.

class notice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    class Meta:
        db_table = 'notice'
    
    def __str__(self):
        return self.title

class ecard(models.Model):
    id = models.AutoField(primary_key=True)
    ownerid = models.IntegerField(unique=True)
    imgpath = models.CharField(max_length=255)

class company(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=255)
    master = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    photo = models.URLField(max_length=255)
    website = models.URLField(max_length=255)
    introduce = models.TextField()
    project = models.TextField()
    class Meta:
        db_table = 'company'
    
    def __str__(self):
        return self.name

class person(models.Model):
    id = models.AutoField(primary_key=True)
    unique = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    introduce = models.TextField()
    
    class Meta:
        db_table = 'person'
    
    def __str__(self):
        return self.name

class government(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'government'

    def __str__(self):
        return self.name

class governmentContact(models.Model):
    id = models.AutoField(primary_key=True)
    contacttype = models.CharField(max_length=255)
    governmentid = models.IntegerField()
    contactor = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    class Meta:
        db_table = 'governmentContact'
    
    def __str__(self):
        return self.contactor