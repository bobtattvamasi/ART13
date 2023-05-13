# myapp/urls.py

from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', include('services.urls')),
    path('appointments/', include('appointments.urls')),
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
    path('users/', include('users.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
]

# myapp/views.py
#
# from django.shortcuts import render
#
# def home(request):
#     return render(request, 'myapp/templates/crm/home.html')
#
# def about(request):
#     return render(request, 'myapp/templates/crm/about.html')
#
# def contact(request):
#     return render(request, 'myapp/templates/crm/contact.html')