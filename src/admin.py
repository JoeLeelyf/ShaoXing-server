from django.contrib import admin
from .models import notice,ecard,company,person,government,governmentContact
# Register your models here.

admin.site.register(notice)
admin.site.register(ecard)
admin.site.register(company)
admin.site.register(person)
admin.site.register(government)
admin.site.register(governmentContact)