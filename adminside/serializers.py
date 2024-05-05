from rest_framework.serializers import ModelSerializer
from vendors.serializers import *
from rest_framework import serializers
from .models import *
# from .models import Vendor


class VendorNotificationSerializer(ModelSerializer):
    class Meta:
        model = VendorNotification
        fields = "__all__"


class VendorNotificationListSerializer(ModelSerializer):
    company = VendorListSerializer()

    class Meta:
        model = VendorNotification
        fields = "__all__"
