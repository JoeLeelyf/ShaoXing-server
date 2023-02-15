from django.contrib import admin
from .models import policy, career, tech, wxUser
# Register your models here.
admin.site.register(policy)
admin.site.register(career)
admin.site.register(tech)
admin.site.register(wxUser)
