from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import  permissions, status
from . serializers import *
from . models import Drug
from rest_framework.response import Response
# Create your views here.

class PharmacyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        drugs = Drug.objects.all()
        serializer = PharmacySerializer(drugs, many=True, context={"request" :request})
        return Response(serializer.data, status=status.HTTP_200_OK)
