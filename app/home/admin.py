# coding: utf-8

from django.contrib import admin
from django.contrib.auth.models import User
from app.home.models import UserProfile,Education,Expertise, FloorPlan
from app.company.models import Company,CompanyStatus
from app.home.forms import UserForm

class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['image_thumb']

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['image_thumb']

admin.site.register(Expertise)
admin.site.register(Education)
admin.site.register(FloorPlan)
admin.site.register(UserProfile)




