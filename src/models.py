from django.db import models
from database.models import wxUser

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
