from django.db import models

# Create your models here.

class notice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    class Meta:
        db_table = 'notice'
    
    def __str__(self):
        return self.title