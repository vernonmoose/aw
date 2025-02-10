from rest_framework import serializers
from . models import Drug

class PharmacySerializer(serializers.ModelSerializer):
    expiry_status = serializers.SerializerMethodField()
    class Meta:
        model = Drug
        fields = "__all__"
        
    def get_expiry_status(self, obj):
        return obj.get_expiry_status()
    
    def get_photo_url(self, obj):
        request = self.context.get("request")
        url = obj.fingerprint.url
        return request.build_absolute_url(url) 