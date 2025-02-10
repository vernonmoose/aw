from django.db import models
from django.contrib.auth import get_user_model
from app.models import Doctor
from pharmacy.models import Drug
from appointment.models import Appointment
User = get_user_model()

class MedicalRecords(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_pressure = models.CharField(max_length=20, null=True, blank=True)
    heart_rate = models.IntegerField(null=True, blank=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_of_vitals = models.DateField()

    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name

class LabResult(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    result = models.TextField()
    normal_range = models.CharField(max_length=255)
    date_of_test = models.DateField()

    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name + "  Test:  " + self.test_name
    
class HealthRecord(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING)
    date_of_record = models.DateField(auto_now_add=True)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    medications_prescribed = models.ManyToManyField(Drug, related_name='health_records', blank=True)
    medication_dosage = models.CharField(max_length=255, blank=True)
    lab_results = models.ForeignKey(LabResult, on_delete=models.CASCADE, null=True, blank=True)
    next_appointment = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name + f" {self.date_of_record} "
