from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from users.permissions import *
from .serializers import *
from .models import *
from django.http import Http404
from users.models import User

# Create your views here.
# listing notifications


class RetrieveVendorNotification(ListAPIView):
    permission_classes = [IsSuperUser]
    queryset = VendorNotification.objects.all()
    serializer_class = VendorNotificationListSerializer


class VendorNotificationEdit(RetrieveUpdateAPIView):
    permission_classes = [IsSuperUser]
    queryset = VendorNotification.objects.all().order_by('id')
    serializer_class = VendorNotificationSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        company = instance.company

        if 'is_approved' in request.data:
            is_approved = request.data['is_approved']
            company.is_approved = is_approved
            if is_approved:
                company.approved_status = "Verified"
            else:
                company.approved_status = "Rejected"
            company.save()

        return Response(serializer.data)

# all users listing


class RetrieveAllUsers(ListAPIView):
    permission_classes = [IsSuperUser]
    queryset = User.objects.filter(
        is_superuser=False, is_vendor=False).order_by('id')
    serializer_class = userDataSerializer

# vendors Listing


class RetrieveAllVendors(ListAPIView):
    permission_classes = [IsSuperUser]
    queryset = CompanyProfile.objects.all().order_by('id')
    serializer_class = VendorSerializer

# Block and unblock user


class BlockAndUnBlockUser(APIView):
    permission_classes = [IsSuperUser]

    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id, is_superuser=False)
        except User.DoesNotExist:
            raise Http404

    def patch(self, request, user_id):
        user = self.get_object(user_id)
        user.is_active = not user.is_active
        user.save()

        return Response({'message': 'User status updated successfully'}, status=status.HTTP_200_OK)


class BlockAndUnBlockVendor(APIView):
    permission_classes = [IsSuperUser]

    def get_object(self, company_id):
        try:
            return CompanyProfile.objects.get(id=company_id)
        except CompanyProfile.DoesNotExist:
            raise Http404

    def patch(self, request, company_id):
        vendor = self.get_object(company_id)
        vendor.is_available = not vendor.is_available
        vendor.save()

        return Response({'message': 'Vendor status updated successfully'}, status=status.HTTP_200_OK)
