from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from .search_views import *
router = DefaultRouter()

router.register(r'enquiry_search', EnquirySearch, basename='enquiry-search')

urlpatterns = [
    path('company_profile_add/', CompanyProfileAdd.as_view(), name='VendorAdd'),
    path('company_profile_edit/<int:pk>/',
         CompanyProfileEdit.as_view(), name='VendorEdit'),

    path('company_service_add/', CompanyServiceAdd.as_view(), name='ServiceAdd'),
    path('company_service_edit/<int:pk>/',
         CompanyServiceEdit.as_view(), name='ServiceEdit'),

    path('enquiry_edit/<int:pk>/', EnquiryEdit.as_view(),
         name='Edit Enquiry status'),

    path('company_sub_service_add/', SubServiceAdd.as_view(), name='SubServiceAdd'),
    path('company_sub_service_edit/<int:pk>/',
         SubServiceEdit.as_view(), name='SubServiceEdit'),

    path('company_hr_employee_add/', HREmployeeAdd.as_view(), name='EmployeeAdd'),
    path('company_hr_employee_edit/<int:pk>/',
         HREmployeeEdit.as_view(), name='EmployeeEdit'),

    path('hr_payroll_add/', HRPayrollAdd.as_view(), name='PayrollAdd'),
    path('hr_payroll_edit/<int:pk>/',
         HRPayrollEdit.as_view(), name='PayrollEdit'),

    path('company_jobs_add/', CompanyJobsAdd.as_view(), name='JobsAdd'),
    path('company_jobs_edit/<int:pk>/',
         CompanyJobsEdit.as_view(), name='JobsEdit'),

    path('document_add/', DocumentsAdd.as_view(), name='Document Creation'),
    path('document_edit/<int:pk>/', DocumentsEdit.as_view(),
         name='Document Editing and Retrieval'),

    path('company_leads_add/', CompanyLeadGenerationAdd.as_view(), name='LeadsAdd'),
    path('company_leads_edit/<int:pk>/',
         CompanyLeadGenerationEdit.as_view(), name='LeadsEdit'),


    path('service_promotion_add/',
         ServicePromotionsAdd.as_view(), name='PromotionAdd'),
    path('service_promotion_edit/<int:pk>/',
         ServicePromotionsEdit.as_view(), name='PromotionEdit'),


    # Fetching last id's
    path('retrieve_last_lead_id/<int:company_id>/',
         lead_generation_last_id.as_view(), name='RetrieveLeadId'),
    path('retrieve_last_employee_id/<int:company_id>/',
         hr_employee_last_id.as_view(), name='RetrieveEmployeeId'),
    path('retrieve_pay_roll_individual/<str:employee_id>/<int:company_id>/',
         retrieve_employee_individual.as_view()),

    # List API urls are under this command line
    path('company_service_retrieve/<int:company_id>/',
         RetrieveCompanyServices.as_view(), name='ServiceRetrieval'),
    path('retrieve_enquiries/<int:company_id>/',
         RetrieveEnquiries.as_view(), name='Retrieve Enquiries'),
    path('company_retrieve/',
         RetrieveCompanyDetails.as_view(), name="CompanyRetrieval"),
    path('sub_service_retrieve/<int:company_id>/',
         RetrieveSubService.as_view(), name='SubServiceRetrieval'),
    path('enquiry_retrieve/<int:company_id>/',
         RetrieveEnquiry.as_view(), name='EnquiryRetrieval'),
    path('jobs_retrieve/<int:company_id>/',
         RetrieveJobs.as_view(), name='JobsRetrieval'),
    path('leads_retrieve/<int:company_id>/',
         RetrieveLeadGeneration.as_view(), name='LeadsRetrieval'),
    path('hr_employee_retrieve/<int:company_id>/',
         RetrieveHREmployees.as_view(), name='HrEmployeeRetrieval'),
    path('hr_payroll_retrieve/<int:company_id>/',
         RetrievePayroll.as_view(), name='PayrollRetrieval'),
    path('service_promotion_retrieve/<int:company_id>/',
         RetrieveServicePromotion.as_view(), name='PromotionRetrieval'),
    path('company_documents_retrieve/<int:company_id>/',
         RetrieveDocuments.as_view(), name='All Documents Retrieval '),
    path('business_card_retrieve/<int:company_id>/',
         RetrieveBusinessCards.as_view(), name='business card retrieve'),
    path('retrieve_card_qr_info/<int:card_id>/', RetrieveBusinessCardQrInfo.as_view(),
         name='qr code retrieval of business card'),
    path('individual_card_retrieve/<str:email>/',
         IndividualBusinessCardRetrieve.as_view(), name="RetrieveIndividualBusinessCards"),
    path('retrieve_company_qr_info/<int:company_id>/',
         RetrieveCompanyCardQrInfo.as_view(), name="qrcode_retrieval_of_company_Profile"), 
    path('company_profile_view/<str:company_url>/',
         RetrieveCompanyProfileDynamic.as_view(), name="company_profile_view"),
    # search url
    path('', include(router.urls)),
]
