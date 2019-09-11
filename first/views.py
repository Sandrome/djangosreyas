from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Employee

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'emp': 'employees'})

def employee_detail(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        raise Http404('Employee does not exist')
    return render(request, 'employee_detail.html', {'employee': employee})    