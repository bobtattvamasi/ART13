# myapp/views.py

from django.shortcuts import render, redirect
from users.models import Customer

def home(request):
    customers = Customer.objects.all()
    return render(request, 'crm/home.html', {'customers': customers})

def about(request):
    return render(request, 'crm/about.html')

def contact(request):
    return render(request, 'crm/contact.html')