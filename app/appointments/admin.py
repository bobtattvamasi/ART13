from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('barber', 'customer', 'date_time', 'duration')