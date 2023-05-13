# users/views.py
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, redirect

def add_customer(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'crm/add_customer.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def customer_added(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New customer has been added!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'crm/customer_added.html', {'form': form})

def login_view(request):
    # TODO: implement login view
    pass