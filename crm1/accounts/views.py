from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    tasks = Task.objects.all()

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'total_orders': total_orders, 'orders': orders, 'pending': pending, 'customers': customers,
               'tasks': tasks, 'total_customers': total_customers, 'delivered': delivered}
    return render(request, 'accounts/dashboard.html', context)


def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'accounts/tasks.html', context)


def customer(request):
    return render(request, 'accounts/customer.html')
