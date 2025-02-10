from django.urls import path, include
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('', index, name="index"),
    path('doctors/', DoctorsView.as_view(), name="doctors"),
    path('doctors/<int:doctor_id>/', DoctorsView.as_view(), name="single-doctor"),
    path('doctors/search/', DoctorSearchView.as_view(), name="single-doctor"),
    path('specializations/', SpecializationView.as_view(), name="specializations"),

    #dcotor Profile
    path('doctor/profile/', DoctorsProfileiew.as_view(), name="doctor-profile"),
    path('doctor/profile/update/', DoctorsView.as_view(), name="doctor-profile-update"),

    # doctor Patients
    path('doctor/patients/', DoctorPatientsView.as_view(), name="doctor-patients"),
    path('doctor/patients/<int:patient_id>/', DoctorPatientsView.as_view(), name="doctor-patients-single"),
    path('doctor/patients/search/', DoctorPatientsSearchView.as_view(), name="doctor-patients-search"),
    path('doctor/data/', DoctorDataView.as_view(), name="doctor-data"),

    #auth
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', LogInView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('reset-password/', index, name="reset-password"),
    path('verify-otp/', index, name="verify-otp"),
    path('create-password/', index, name="create-password"),

    #Other Apps
    path('appointments/', include("appointment.urls")),
    path('healthtips/', include("healthtips.urls")),
    path('pharmacy/', include("pharmacy.urls")),
    path('healthrecord/', include("healthrecord.urls")),

]