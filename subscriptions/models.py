from django.db import models
from users.models import User
# Create your models here.


# class CardDetails(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     card_number = models.CharField(max_length=30)
#     expiry_date = models.DateField()
#     cvv = models.IntegerField()
#     card_holder_name = models.CharField(max_length=20)
#     name_of_card = models.CharField(max_length=20)
#     is_default = models.BooleanField(default=False)
#     is_available = models.BooleanField(default=True)
