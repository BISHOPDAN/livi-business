from django.contrib import admin

from .models import User, VerificationOtp

# Register your models here.
admin.site.register(User)
admin.site.register(VerificationOtp)
