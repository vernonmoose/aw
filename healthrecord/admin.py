from django.contrib import admin
from.models import HealthRecord, MedicalRecords,LabResult
# Register your models here.
admin.site.register(HealthRecord)
admin.site.register(MedicalRecords)
admin.site.register(LabResult)