from django.db import models
import datetime

# Create your models here.
class policy(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.datetime.now)
    unit = models.CharField(max_length=255)
    content = models.TextField()
    class Meta:
        db_table = 'police'
    
    def __str__(self):
        return self.title

class career(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.datetime.now)
    unit = models.CharField(max_length=255)
    content = models.TextField()
    class Meta:
        db_table = 'career'
    
    def __str__(self):
        return self.title

class tech(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(max_length=255)
    class Meta:
        db_table = 'tech'
    
    def __str__(self):
        return self.title