from django.contrib import admin

from .models import Employee
from .models import Interests

@admin.register(Interests)
class InterestsAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','role','age','sex']