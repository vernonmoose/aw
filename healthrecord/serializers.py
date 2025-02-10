from rest_framework import serializers
from . models import HealthRecord
from rest_framework.exceptions import ValidationError

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = "__all__"
    
    def validate(self, attrs):
        pass

    def create(self, clean_data):
        pass
