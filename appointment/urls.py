from django.urls import path
from . views import *

urlpatterns = [
    path('', AppointmentView.as_view(), name="appointment"),
]