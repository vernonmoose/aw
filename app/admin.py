from django.contrib import admin
from . models import User, Doctor, Specialization
# Register your models here.
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Specialization)