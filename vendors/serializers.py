from rest_framework.serializers import ModelSerializer
from users.serializers import *
from rest_framework import serializers
from .models import *
# from .models import Vendor


class VendorSerializer(ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = "__all__"


class VendorListSerializer(ModelSerializer):
    user = userDataSerializer()

    class Meta:
        model = CompanyProfile
        fields = "__all__"

# Service Serializers


class CompanyServiceSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Check if the service_name is unique within the same company.
        company_id = data.get('company_id')
        service_name = data.get('service_name')
        instance = self.instance
        if instance:
            existing_service = CompanyServices.objects.filter(
                company_id=company_id, service_name=service_name).exclude(pk=instance.pk)
        else:
            existing_service = CompanyServices.objects.filter(
                company_id=company_id, service_name=service_name)
        if existing_service.exists():
            raise serializers.ValidationError(
                'A service with the same name already exists for this company.')

        return data

    class Meta:
        model = CompanyServices
        fields = "__all__"


class CompanyServiceListSerializer(ModelSerializer):
    company_id = VendorSerializer()

    class Meta:
        model = CompanyServices
        fields = "__all__"

# Sub service Serializers


class CompanySubServiceSerializer(ModelSerializer):
    class Meta:
        model = CompanySubServices
        fields = "__all__"


class CompanySubServiceListSerializer(ModelSerializer):
    company_services = CompanyServiceListSerializer()

    class Meta:
        model = CompanySubServices
        fields = "__all__"

# Enquiry Serializers


class CompanyEnquirySerializer(ModelSerializer):
    class Meta:
        model = CompanyEnquiry
        fields = "__all__"


class CompanyEnquiryListSerializer(ModelSerializer):
    user = userDataSerializer()
    sub_service = CompanySubServiceSerializer()

    class Meta:
        model = CompanyEnquiry
        fields = "__all__"


# Jobs Serializers
class CompanyJobsSerializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"


class CompanyJobsListSerializer(ModelSerializer):
    company = VendorListSerializer()

    class Meta:
        model = Jobs
        fields = "__all__"


# Lead generation Serializer
class CompanyLeadGenerationSerializer(ModelSerializer):

    class Meta:
        model = LeadGeneration
        fields = "__all__"


class CompanyLeadGenerationLisSerializer(ModelSerializer):
    company = VendorListSerializer()

    class Meta:
        model = LeadGeneration
        fields = "__all__"


# HR System Employee Serializer
class CompanyHREmployeeSerializer(ModelSerializer):

    class Meta:
        model = HREmployees
        fields = "__all__"


class CompanyHREmployeeListSerializer(ModelSerializer):
    company = VendorSerializer()

    class Meta:
        model = HREmployees
        fields = "__all__"


# HR Employee Payroll Serializer
class HRPayrollSerializer(ModelSerializer):

    class Meta:
        model = Payroll
        fields = "__all__"


class HRPayrollListSerializer(ModelSerializer):
    employee = CompanyHREmployeeListSerializer()

    class Meta:
        model = Payroll
        fields = "__all__"

# Service Promotion Serializer


class ServicePromotionSerializer(ModelSerializer):

    class Meta:
        model = CompanyServicePromotion
        fields = "__all__"


class ServicePromotionListSerializer(ModelSerializer):
    company_id = VendorSerializer()
    service_id = CompanyServiceSerializer()
    sub_service_id = CompanySubServiceSerializer()

    class Meta:
        model = CompanyServicePromotion
        fields = "__all__"

# Document Serializer


class DocumentsSerializer(ModelSerializer):

    class Meta:
        model = CompanyDocuments
        fields = "__all__"


class DocumentsListSerializer(ModelSerializer):
    company = VendorSerializer()

    class Meta:
        model = CompanyDocuments
        fields = "__all__"

# Business Card Serializer


class BusinessCardSerializer(ModelSerializer):

    class Meta:
        model = BusinessCards
        fields = "__all__"


class BusinessCardListSerializer(ModelSerializer):
    company = VendorSerializer()
    hr_employee = CompanyHREmployeeSerializer()

    class Meta:
        model = BusinessCards
        fields = "__all__"


class BusinessCardQrListSerializer(ModelSerializer):
    business_card = BusinessCardListSerializer()

    class Meta:
        model = QrCodeForBusinessCard
        fields = "__all__"

class CompanyQrListSerializer(ModelSerializer):
    company = VendorListSerializer()

    class Meta:
        model = QrCodeForCompany
        fields = "__all__"