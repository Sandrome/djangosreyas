from django.contrib import admin
from django.urls import path
from django.urls import re_path

from first import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^employee/(\d+)/', views.employee_detail, name='employee_details'),
    re_path(r'emp_form/', views.emp_form, name='emp_form'),
]
