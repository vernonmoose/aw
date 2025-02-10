from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from . models import HealthRecord
from django.shortcuts import get_object_or_404
from .serializers import *
from django.contrib.auth import get_user_model
from appointment.models import Appointment
from app.models import Doctor
from app.permissions import IsDoctor
User = get_user_model()

class HealthRecordView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def get(self, request, patient_id=None):
        if patient_id is not None:
            patient = get_object_or_404(User, id=patient_id)
            record = get_object_or_404(HealthRecord, patient=patient)
            serializer = HealthRecordSerializer(record, context={"request" : request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        records = HealthRecord.objects.all()
        serializer = HealthRecordSerializer(records, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data

        appontment_id =  data.get("appointment_id")
        appointment = get_object_or_404(Appointment, id=appontment_id)
        doctor = Doctor.objects.filter(user=request.user).first()
        patient = get_object_or_404(User, id=data.get("patient_id"))
        
        if appointment.doctor != doctor:
            return Response({"detail" : f" Patient {patient.first_name} {patient.last_name} id not your patient!"}, status=status.HTTP_403_FORBIDDEN)

        serializer = HealthRecordSerializer(data=data)
        if serializer.si_valid(raise_exception=True):
            serializer.save()
            return Response({"detail" : "Health Record created succesfully!"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        
