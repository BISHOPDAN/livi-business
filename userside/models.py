from django.db import models
from users.models import User
from phonenumber_field.modelfields import PhoneNumberField
from vendors.models import Jobs


# Create your models here.


class JobApplication(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NIL', 'Nil'),
    )

    MARITAL_CHOICES = (
        ('S', 'Single'),
        ('M', 'Married'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)
    date_of_birth = models.DateField()
    total_years_of_experience = models.IntegerField()
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    current_location = models.CharField(max_length=100)
    preferred_location = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=1, choices=MARITAL_CHOICES)
    qualification = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    description = models.TextField()
    upload_resume = models.FileField(upload_to='resumes/')
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.full_name
