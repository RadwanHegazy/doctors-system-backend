from django.contrib import admin
from django.contrib.auth.models import  Group
from .models import Doctor, Department, DoctorModel

admin.site.unregister(Group)




class DocPanel (admin.ModelAdmin) : 
    list_display = ('full_name','email','department',)

admin.site.register(DoctorModel,DocPanel)
admin.site.register(Department)