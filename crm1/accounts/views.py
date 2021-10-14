from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from .models import *


def home(request):
    return render(request, 'accounts/dashboard.html')


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'accounts/tasks.html', {'tasks': tasks})


def customer(request):
    return render(request, 'accounts/customer.html')
