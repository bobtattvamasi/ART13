from django.urls import path
from .views import AppointmentListView, AppointmentCreateView, AppointmentDetailView, AppointmentUpdateView, AppointmentDeleteView

app_name = 'appointments'

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment_list'),
    path('create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
]