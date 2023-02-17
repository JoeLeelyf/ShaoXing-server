from django.db import models

# Create your models here.

class authentication(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = 'authentication'
    
    def __str__(self):
        return self.username