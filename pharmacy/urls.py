from django.urls import path
from . views import *

urlpatterns = [
    path('drugs/', PharmacyView.as_view(), name="appointment"),
]