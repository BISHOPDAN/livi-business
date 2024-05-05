from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import User
from django.core.exceptions import ValidationError
from vendors.models import CompanyProfile
# Create your models here.


class VendorNotification(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_verified = models.CharField(max_length=200)
    
