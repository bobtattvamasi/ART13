# users/urls.py
from django.urls import path
from .views import signup_view, login_view, add_customer, customer_added

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('add-customer/', add_customer, name='add-customer'),
    path('customer-added/', customer_added, name='customer_added'),
]