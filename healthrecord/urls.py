from django.urls import path
from . views import *

urlpatterns = [
    path('', HealthRecordView.as_view(), name="health-record"),
    path('<int:patient_id>', HealthRecordView.as_view(), name="health-record-single"),
    path('<int:patient_id>/update/', HealthRecordView.as_view(), name="health-record-single"),
]