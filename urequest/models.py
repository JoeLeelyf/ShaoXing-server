from django.db import models

# Create your models here.

class authentication(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cardtype = models.CharField(max_length=255)
    cardnum = models.CharField(max_length=255)
    currentunit = models.CharField(max_length=255)
    class Meta:
        db_table = 'authentication'
    
    def __str__(self):
        return self.name

class jobexperience(models.Model):
    id = models.AutoField(primary_key=True)
    auth = models.ForeignKey(authentication, on_delete=models.CASCADE)
    unitname = models.CharField(max_length=255)
    unitaddress = models.CharField(max_length=255)
    starttime = models.CharField(max_length=255)
    endtime = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    typeJobExp = models.CharField(max_length=255)
    class Meta:
        db_table = 'jobexperience'
    
    def __str__(self):
        return self.unitname

class eduexperience(models.Model):
    id = models.AutoField(primary_key=True)
    auth = models.ForeignKey(authentication, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    edulevel = models.CharField(max_length=255)
    starttime = models.CharField(max_length=255)
    endtime = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    class Meta:
        db_table = 'eduexperience'
    
    def __str__(self):
        return self.school


class persontype(models.Model):
    id = models.AutoField(primary_key=True)
    auth = models.ForeignKey(authentication, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    class Meta:
        db_table = 'persontype'
    
    def __str__(self):
        return self.type