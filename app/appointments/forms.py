from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ['barber', 'customer', 'date_time', 'duration']

		def clean(self):
		    cleaned_data = super().clean()
		    date_time = cleaned_data.get('date_time')
		    duration = cleaned_data.get('duration')
		    if date_time and duration:
		        end_time = date_time + timezone.timedelta(minutes=duration)
		        appointments = Appointment.objects.filter(date_time__lte=end_time, date_time__gte=date_time)
		        if appointments.exists():
		            raise forms.ValidationError("This barber already has an appointment at this time.")
		    return cleaned_data
