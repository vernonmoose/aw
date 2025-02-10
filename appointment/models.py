from django.db import models
from django.contrib.auth import get_user_model
from app.models import Doctor
from django.core.validators import RegexValidator
User = get_user_model()

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    phone_no = models.CharField(
        max_length=13, 
        validators=[RegexValidator(r'^\+?1?\d{9,13}$', 'Enter a valid phone number.')]
    )
    caseInfo = models.TextField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Appointment: {self.patient.first_name} with Dr. {self.doctor.user.first_name} on {self.date}"

