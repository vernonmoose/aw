from rest_framework import serializers
from .models import HealthTip, Paragraph
from django.contrib.auth import get_user_model

User = get_user_model()

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'content', 'order']

class HealthTipsSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()
    content = ParagraphSerializer(many=True, source='paragraphs') 

    class Meta:
        model = HealthTip
        fields = ['id', 'title', 'image', 'doctor_name', 'content']

    def get_doctor_name(self, obj):
        return obj.author.get_full_name()
