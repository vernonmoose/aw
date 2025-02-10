from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions, status, authentication
from rest_framework.views import APIView
from . serializers import *
from .models import HealthTip

class HealthTipsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = HealthTip.objects.all()
        serializer = HealthTipsSerializer(queryset, many=True, context={"request" : request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        pass
    
