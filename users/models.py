from datetime import datetime
import datetime
import time
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
import phonenumbers
from .managers import CustomUserManager
from datetime import date, timedelta

class CustomUser(AbstractBaseUser, PermissionsMixin):  

    alphabits = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabits characters are allowed.')

    username=models.CharField(max_length=20,null=True)
    firstname=models.CharField(max_length=50, validators=[alphabits])
    lastname=models.CharField(max_length=50, validators=[alphabits])
    email=models.EmailField(max_length=50,unique=True)
    dob = models.DateField(null=True, blank=False)
    age = models.IntegerField(null=True, blank=False)
    phone_numbers=PhoneNumberField(null=True,unique=True)
    address=models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    
    def __str__(self):
        return self.email
    

    def Age(self):
        if self.dob is not None:
            self.Age = (date.today() - self.dob) // timedelta(days=365.2425)
        
        return self.Age