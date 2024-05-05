from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializers import *


class CustomerSearch(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer_name', 'contact_number',
                     'email', 'city', 'address', 'country']

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = Customer.objects.filter(company=company_id)
        return queryset


class SupplierSearch(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['supplier_name', 'email', 'contact_number', 'item_name']
    queryset = None

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = Supplier.objects.filter(company=company_id)
        return queryset


class ExpenseSearch(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['amount_paid', 'created_at',
                     'payment_type', 'to__customer_name']

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = Expense.objects.filter(company=company_id)
        return queryset


class DailyRegisterSearch(viewsets.ModelViewSet):
    serializer_class = DailyRegisterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_id', 'order_date',
                     'client', 'customer__customer_name', 'work_type']

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = DailyRegister.objects.filter(company=company_id)
        return queryset


class QuotationsSearch(viewsets.ModelViewSet):
    serializer_class = QuotationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['quotation_identifier', 'quotation_date',
                     'quotation_status', 'customer__customer_name']

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = Quotation.objects.filter(company=company_id)
        return queryset


class PurchaseSearch(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['supplier__supplier_name',
                     'supplier__contact_number', 'item_purchase', 'purchase_date']

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = Purchase.objects.filter(company=company_id)
        return queryset


class InvoiceSearch(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['invoice_identifier', 'order_id__order_id',
                     'customer__customer_name', 'invoice_date', 'invoice_amount']

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = StatementOfAccounts.objects.filter(company=company_id)
        return queryset


class PaymentCollectionSearch(viewsets.ModelViewSet):
    serializer_class = PaymentCollectionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer__customer_name',
                     'payment_date', 'payment_type', '']

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = PaymentCollections.objects.filter(company=company_id)
        return queryset
