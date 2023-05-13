# from django.shortcuts import render, get_object_or_404
# from .models import Appointment

# def appointment_list(request):
#     appointments = Appointment.objects.all()
#     return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

# def appointment_detail(request, pk):
#     appointment = get_object_or_404(Appointment, pk=pk)
#     return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Appointment

class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'
    ordering = ['-date_time']

class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['barber', 'customer', 'date_time', 'duration']

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['barber', 'customer', 'date_time', 'duration']

class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointments:appointment-list')

