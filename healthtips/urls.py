from django.urls import path
from . views import * 

urlpatterns = [
    path('', HealthTipsView.as_view(), name="tips"),
]