# appointments/models.py

# from django.db import models

# class Appointment(models.Model):
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     customer_name = models.CharField(max_length=100)
#     appointment_date = models.DateField()
#     appointment_time = models.TimeField()

from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import Barber, Customer

class Appointment(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer}'s appointment with {self.barber} on {self.date_time}"

    def get_absolute_url(self):
        return reverse('appointments:appointment-detail', kwargs={'pk': self.pk})
