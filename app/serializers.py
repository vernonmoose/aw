from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from . models import Doctor, Specialization
from appointment.models import Appointment
User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError({"message" : "Email already exists!"})
        return super().validate(attrs)
    
    def create(self, clean_data):
        user = User.objects.create_user(email=clean_data['email'],  
                                        first_name=clean_data['first_name'], 
                                        last_name=clean_data['last_name'], 
                                        password=clean_data['password'])
         
        user.save()
        return user
    
class LoginSerializer(serializers.ModelSerializer): 
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email","password"]

    def check_user (self, clean_data):
        user = authenticate(email=clean_data['email'], password=clean_data['password'])
        if not user:
            raise ValidationError("User not found")
        else:
            return user
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    education = serializers.SerializerMethodField()
    contact = serializers.SerializerMethodField()
    work_schedule = serializers.SerializerMethodField()
    specialization = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ["id",'name', 'specialization', 'education', 'contact', 'work_schedule', 'about', "image", ]

    def get_education(self, obj):
        """Return the education details"""
        return {
            'degree': obj.degree,
            'institution': obj.institution,
            'graduation_year': obj.graduation_year
        }

    def get_contact(self, obj):
        """Return the contact details"""
        return {
            'phone': obj.phone_no,
            'telegram': obj.telegram
        }

    def get_work_schedule(self, obj):
        """Return the work schedule with days and time range."""
        work_from = obj.work_from.strftime('%H:%M %p')
        work_to = obj.work_to.strftime('%H:%M %p')
        time_range = f"{work_from} - {work_to}"
        return {
            'days': obj.get_days(), 
            'time': time_range
        }
    def get_specialization(self, obj):
        return obj.specialization.specialist
    
    def get_photo_url(self, obj):
        request = self.context.get("request")
        url = obj.fingerprint.url
        return request.build_absolute_url(url) 
    
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"

class DoctorSearchSerializer(serializers.Serializer):
    pass


#Doctor Patients serializer

class DoctorPatientsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Appointment
        fields = "__all__"
    
    def get_name(self, obj):
        return obj.patient.get_full_name()

class DoctorPatientsSearchView(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

class DoctorDataSerializer(serializers.Serializer):
    pass