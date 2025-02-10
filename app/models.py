from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import RegexValidator
from django.utils.timezone import now

# def patient_directory_path(instance, filename):
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

def doctor_directory_path(instance, filename):
    return 'doctors/doctor_{0}/{1}'.format(instance.user.id, filename)

class UserManager(BaseUserManager):
    def create_user (self, email, first_name, last_name, password=None, is_active=True, is_staff=False, is_admin=False, is_doctor=False):
        if not email:
            raise ValueError("User must have email")
        if not password:
            raise ValueError("User must have password")
        if not first_name:
            raise ValueError("User must have first name")
        if not last_name:
            raise ValueError("User must have last name")
        
        email = self.normalize_email(email)
        user = self.model( 
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.doctor = is_doctor
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, first_name,last_name, password=None):
        if not email:
            raise ValueError("User must have email")
        if not password:
            raise ValueError("User must have password")
        
        user = self.create_user(
            email, 
            first_name,
            last_name,
            password=password,
            is_staff=True
        )
        return user
    
    def create_superuser(self, email, first_name, last_name ,password=None): 
        if not email:
            raise ValueError("User must have email")
        if not password:
            raise ValueError("User must have password")
        
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, max_length=255, default=None)
    first_name = models.CharField(max_length=150, null=False, default="")
    last_name = models.CharField(max_length=150, null=False, default="")
    active =  models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    doctor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects  = UserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_doctor(self):
        return self.doctor
    
class Specialization(models.Model):
    specialization = models.CharField(max_length=100)
    specialist = models.CharField(max_length=100)

    def __str__(self):
        return self.specialization


class Doctor(models.Model):
    # Days of the week choices
    DAYS_OF_THE_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctorprofile")
    name = models.CharField(max_length=100, default='Unknown', null=True, blank=True)
    image = models.ImageField(null=True, upload_to=doctor_directory_path, blank=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.DO_NOTHING, related_name="doctor_specialization")
    phone_no = models.CharField(
        max_length=13, 
        validators=[RegexValidator(r'^\+?1?\d{9,13}$', 'Enter a valid phone number.')], 
        null=True, 
        blank=True
    )
    
    telegram = models.CharField(max_length=50, null=True, blank=True)
    degree = models.CharField(max_length=300)
    institution = models.CharField(max_length=300)
    graduation_year = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{4}$', 'Enter a valid year.')])
    days = models.CharField(max_length=255, blank=True)
    work_from = models.TimeField()
    work_to = models.TimeField()
    about = models.TextField(max_length=1000)
    location = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or f'Doctor {self.user.username}'

    def set_days(self, days_list):
        """Set the days as a comma-separated string."""
        valid_days = [day for day in days_list if day in dict(self.DAYS_OF_THE_WEEK)]
        self.days = ','.join(valid_days)

    def get_days(self):
        """Return the days as a list."""
        return self.days.split(',') if self.days else []

    def get_absolute_url(self):
        return reverse('doctors', args=[str(self.user.id)])
