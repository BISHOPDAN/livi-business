from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializers import *


class EnquirySearch(viewsets.ModelViewSet):
    serializer_class = CompanyEnquirySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'enquiry_status',
                     'user__phone_number', 'user__email',]

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = CompanyEnquiry.objects.filter(
            sub_service__company_services__company_id=company_id)
        return queryset
