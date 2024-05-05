import os
from datetime import datetime
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView
from users.permissions import *
from .serializers import *
from .models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import qrcode
from rest_framework.permissions import IsAuthenticated
from decouple import config

"""
The edit api can also  retrieve individual data based on the pk

"""
domain = config('front_end_url')


class CompanyProfileAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanyProfile.objects.all()
    serializer_class = VendorSerializer


class CompanyProfileEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanyProfile.objects.all()
    serializer_class = VendorSerializer


class EnquiryEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    serializer_class = CompanyEnquirySerializer
    queryset = CompanyEnquiry.objects.all()


class CompanyServiceAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanyServices.objects.all()
    serializer_class = CompanyServiceSerializer


class CompanyServiceEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanyServices.objects.all()
    serializer_class = CompanyServiceSerializer


class SubServiceAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanySubServices.objects.all()
    serializer_class = CompanySubServiceSerializer


class SubServiceEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanySubServices.objects.all()
    serializer_class = CompanySubServiceSerializer


class CompanyEnquiryAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanyEnquiry.objects.all()
    serializer_class = CompanyEnquirySerializer


class CompanyEnquiryEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanyEnquiry.objects.all()
    serializer_class = CompanyEnquirySerializer


class CompanyJobsAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = Jobs.objects.all()
    serializer_class = CompanyJobsSerializer


class CompanyJobsEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = Jobs.objects.all()
    serializer_class = CompanyJobsSerializer


class lead_generation_last_id(APIView):
    def get(self, *args, **kwargs):
        company_id = kwargs.get('company_id')
        last_lead_id = "0001"  # Default value with leading zeros

        existing_leads = LeadGeneration.objects.filter(company=company_id)
        if existing_leads.exists():
            last_instance = existing_leads.order_by('-lead_id').first()
            # Format with leading zeros
            last_lead_id = str(int(last_instance.lead_id) + 1).zfill(4)

        data = {
            'last_lead_id': last_lead_id
        }
        return Response(data=data, status=status.HTTP_200_OK)


class CompanyLeadGenerationAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = LeadGeneration.objects.all()
    serializer_class = CompanyLeadGenerationSerializer


class CompanyLeadGenerationEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = LeadGeneration.objects.all()
    serializer_class = CompanyLeadGenerationSerializer


class hr_employee_last_id(APIView):
    def get(self, *args, **kwargs):
        company_id = kwargs.get('company_id')
        # Default value set to "0001"
        last_employee_id = "0001"
        existing_employees = HREmployees.objects.filter(company=company_id)
        if existing_employees.exists():
            last_employee = existing_employees.order_by('-employee_id').first()
            last_employee_id = str(int(last_employee.employee_id) + 1).zfill(4)
        else:
            last_employee_id = "0001"
        data = {
            "last_employee_id": last_employee_id
        }
        return Response(data=data, status=status.HTTP_200_OK)


class HREmployeeAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = HREmployees.objects.all()
    serializer_class = CompanyHREmployeeSerializer


class HREmployeeEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = HREmployees.objects.all()
    serializer_class = CompanyHREmployeeSerializer


class HRPayrollAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = Payroll.objects.all()
    serializer_class = HRPayrollSerializer


class HRPayrollEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = Payroll.objects.all()
    serializer_class = HRPayrollSerializer


class retrieve_employee_individual(APIView):
    permission_classes = [IsVendor]

    def get(self, *args, **kwargs):
        try:
            employee_id = kwargs['employee_id']
            company_id = kwargs['company_id']
        except KeyError as e:
            data = {
                "message": f"Missing parameter: {e}"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        employee_instance = HREmployees.objects.filter(
            employee_id=employee_id, company=company_id).first()
        if employee_instance:
            data = {
                "employee_name": f"{employee_instance.first_name} {employee_instance.last_name}",
                "designation": employee_instance.designation,
                "basic_salary": employee_instance.basic_salary,
                "HRA": employee_instance.HRA,
                "transportation_allowance": employee_instance.transportation_allowance,
                "other_allowance": employee_instance.other_allowance
            }
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = {
                "message": "There is no data based on these credentials"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class ServicePromotionsAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanyServicePromotion.objects.all()
    serializer_class = ServicePromotionSerializer


class ServicePromotionsEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanyServicePromotion.objects.all()
    serializer_class = ServicePromotionSerializer


class DocumentsAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanyDocuments.objects.all()
    serializer_class = DocumentsSerializer


class DocumentsEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = CompanyDocuments.objects.all()
    serializer_class = DocumentsSerializer


def create_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Generate unique filename based on current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"qr_code_{timestamp}.png"
    # file_path = os.path.join(os.getcwd(), filename)

    # img.save()
    print(f"QR code saved as ")
    return img


"""
List Api Views are under This command

"""


class RetrieveCompanyServices(ListAPIView):
    serializer_class = CompanyServiceListSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        try:
            queryset = CompanyServices.objects.filter(
                company_id=company_id)
            if not queryset.exists():
                raise Http404(
                    "Company Service does not exist for this company.")
            return queryset
        except CompanyServices.DoesNotExist:
            raise Http404("Company profile does not exist for this user.")


class RetrieveCompanyDetails(ListAPIView):
    serializer_class = VendorListSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        user = self.request.user
        try:
            queryset = CompanyProfile.objects.filter(user=user).order_by('id')
            if not queryset.exists():
                raise Http404("Company profile does not exist for this user.")
            return queryset
        except CompanyProfile.DoesNotExist:
            raise Http404("Company profile does not exist for this user.")


class RetrieveSubService(ListAPIView):
    serializer_class = CompanySubServiceListSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        try:
            queryset = CompanySubServices.objects.filter(
                company_services__company_id=company_id, is_available=True)
            if not queryset.exists():
                raise Http404(
                    "Company Sub Services not exist on this main Service")
            return queryset
        except CompanySubServices.DoesNotExist:
            raise Http404(
                "Company Sub Services not exist on this main Service")


class RetrieveEnquiry(ListAPIView):
    serializer_class = CompanyEnquiryListSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        try:
            queryset = CompanyEnquiry.objects.filter(
                sub_service__company_services__company_id=company_id, is_available=True)
            if not queryset.exists():
                raise Http404("Enquires Does not exist")
            return queryset
        except CompanyEnquiry.DoesNotExist:
            raise Http404("Enquires Does not exist")


class RetrieveJobs(ListAPIView):
    serializer_class = CompanyJobsListSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        try:
            queryset = Jobs.objects.filter(company=company_id)
            if not queryset.exists():
                raise Http404("Jobs not found")
            return queryset
        except Jobs.DoesNotExist:
            raise Http404("Jobs not found")


class RetrieveLeadGeneration(ListAPIView):
    serializer_class = CompanyLeadGenerationLisSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = LeadGeneration.objects.filter(
            company=company_id).order_by('id')
        return queryset
        # try:
        #     queryset = LeadGeneration.objects.filter(company=company_id)
        #     if not queryset.exists():
        #         raise Http404("Leads not found")
        #     return queryset
        # except LeadGeneration.DoesNotExist:
        #     raise Http404("Leads not found")


class RetrieveHREmployees(ListAPIView):
    serializer_class = CompanyHREmployeeListSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = HREmployees.objects.filter(
            company=company_id, is_available=True).order_by('id')
        return queryset

        # try:
        #     queryset = HREmployees.objects.filter(
        #         company=company_id, is_available=True)
        #     if not queryset.exists():
        #         raise Http404("Employees not found")
        #     return queryset
        # except HREmployees.DoesNotExist:
        #     raise Http404("Employees not found")


class RetrievePayroll(ListAPIView):
    serializer_class = HRPayrollListSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = Payroll.objects.filter(
            company=company_id, is_available=True
        ).order_by('id')
        return queryset
        # try:
        #     queryset = Payroll.objects.filter(company=company_id)
        #     if not queryset.exists():
        #         raise Http404("Payroll not found")
        #     return queryset
        # except Payroll.DoesNotExist:
        #     raise Http404("Payroll not found")


class RetrieveServicePromotion(ListAPIView):
    serializer_class = ServicePromotionListSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = CompanyServicePromotion.objects.filter(
            company_id=company_id, is_available=True)
        return queryset
        # try:
        #     queryset = CompanyServicePromotion.objects.filter(
        #         company_id=company_id, is_available=True)
        #     if not queryset.exists():
        #         raise Http404("Promotions not found")
        #     return queryset
        # except CompanyServicePromotion.DoesNotExist:
        #     raise Http404("Promotions not found")


class RetrieveBusinessCards(ListAPIView):
    serializer_class = BusinessCardListSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = BusinessCards.objects.filter(
            company=company_id, is_available=True)
        return queryset


class RetrieveDocuments(ListAPIView):
    serializer_class = DocumentsListSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = CompanyDocuments.objects.filter(
            company_id=company_id, is_available=True).order_by('id')
        return queryset
        # try:
        #     if not queryset.exists():
        #         raise Http404("Documents not found")
        #     return queryset
        # except CompanyDocuments.DoesNotExist:
        #     raise Http404("Documents not found")


class RetrieveEnquiries(APIView):
    serializer_class = CompanyEnquiryListSerializer
    permission_classes = [IsVendor]

    def get(self, request, company_id):
        try:
            # Get total count of all enquiries
            total_enquiries_count = CompanyEnquiry.objects.count()
            queryset = CompanyEnquiry.objects.filter(
                sub_service__company_services__company_id=company_id, is_available=True)
            if not queryset.exists():
                raise Http404("Documents not found")
            serializer = self.serializer_class(queryset, many=True)
            response_data = {
                'total_enquiries_count': total_enquiries_count,
                'enquiries': serializer.data
            }
            return Response(response_data)

        except CompanyEnquiry.DoesNotExist:
            raise Http404("Enquiries not found")


class RetrieveBusinessCardQrInfo(ListAPIView):
    serializer_class = BusinessCardQrListSerializer

    def get_queryset(self):
        card_id = self.kwargs.get('card_id')
        queryset = QrCodeForBusinessCard.objects.filter(business_card=card_id)

        return queryset


class IndividualBusinessCardRetrieve(ListAPIView):
    serializer_class = BusinessCardQrListSerializer

    def get_queryset(self):
        email = self.kwargs.get('email')
        queryset = QrCodeForBusinessCard.objects.filter(
            business_card__hr_employee__email=email)
        return queryset


class RetrieveCompanyCardQrInfo(ListAPIView):
    serializer_class = CompanyQrListSerializer

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = QrCodeForCompany.objects.filter(company=company_id)
        return queryset
        
class RetrieveCompanyProfileDynamic(ListAPIView):
    serializer_class = CompanyQrListSerializer
    def get_queryset(self):
        company_url = self.kwargs.get('company_url')        
        company_urls=f"{domain}{company_url}/"
        queryset = QrCodeForCompany.objects.filter(url=company_urls)
        return queryset    