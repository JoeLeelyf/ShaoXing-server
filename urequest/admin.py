from django.contrib import admin
from .models import authentication, jobexperience, eduexperience, persontype
# Register your models here.

admin.site.register(authentication)
admin.site.register(jobexperience)
admin.site.register(eduexperience)
admin.site.register(persontype)