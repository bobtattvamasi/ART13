from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)

# services/views.py

from django.shortcuts import render
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})
