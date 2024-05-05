from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView
from users.permissions import *
from .serializers import *
from .models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class CustomerAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SupplierAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class DailyRegisterAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = DailyRegister.objects.all()
    serializer_class = DailyRegisterSerializer


class DailyRegisterEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = DailyRegister.objects.all()
    serializer_class = DailyRegisterSerializer


class retrieve_last_order_id(APIView):

    def get(self, request, *args, **kwargs):
        default_order_id = "DR0001"
        company_id = kwargs.get('company_id')
        existing_instances = DailyRegister.objects.filter(company=company_id)

        if existing_instances.exists():
            last_daily_register_instance = existing_instances.order_by(
                '-order_id').first()
            last_order_id_numeric_part = int(
                last_daily_register_instance.order_id[2:])  # Extract numeric part
            next_order_id_numeric_part = last_order_id_numeric_part + 1
            # Pad with leading zeros
            next_order_id = f"DR{str(next_order_id_numeric_part).zfill(4)}"
            return Response(data=next_order_id, status=status.HTTP_200_OK)

        else:
            return Response(data=default_order_id, status=status.HTTP_200_OK)


class QuotationAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer


class QuotationEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer


class QuotationItemAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = QuotationItems.objects.all()
    serializer_class = QuotationItemSerializer


class QuotationItemEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = QuotationItems.objects.all()
    serializer_class = QuotationItemSerializer


class retrieve_last_quotation_id(APIView):
    def get(self, request, company_id):
        try:
            default_id = "QU0001"
            existing_quotations = Quotation.objects.filter(
                company=company_id)
            if existing_quotations.exists():
                last_quotation = existing_quotations.order_by(
                    '-quotation_identifier').first()
                last_quotation_numeric_id = int(
                    last_quotation.quotation_identifier[2:])

                next_quotation_id_numeric_part = last_quotation_numeric_id + 1
                next_quotation_id = f"QU{str(next_quotation_id_numeric_part).zfill(4)}"
                return Response(data=next_quotation_id, status=status.HTTP_200_OK)
            else:
                return Response(data=default_id, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PurchaseAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class ExpenseAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class InvoiceAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = StatementOfAccounts.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = StatementOfAccounts.objects.all()
    serializer_class = InvoiceSerializer


class retrieve_invoice_id(APIView):
    def get(self, request, company_id):
        try:
            existing_instances = StatementOfAccounts.objects.filter(
                company=company_id)
            if existing_instances.exists():
                last_instance = existing_instances.order_by(
                    '-invoice_identifier').first()
                last_instance_numeric_id = int(
                    last_instance.invoice_identifier[3:])
                next_invoice_identifier_numeric_part = last_instance_numeric_id + 1
                next_invoice_id = f"INV{str(next_invoice_identifier_numeric_part).zfill(3)}"
                return Response(data=next_invoice_id, status=status.HTTP_200_OK)
            else:
                return Response(data="INV001", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentCollectionAdd(CreateAPIView):
    permission_classes = [IsVendor]
    queryset = PaymentCollections
    serializer_class = PaymentCollectionSerializer


class PaymentCollectionEdit(RetrieveUpdateAPIView):
    permission_classes = [IsVendor]
    queryset = PaymentCollections
    serializer_class = PaymentCollectionSerializer


"""
List Api Views
"""


class RetrieveCustomers(ListAPIView):
    permission_classes = [IsVendor]
    serializer_class = CustomerListSerializer

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = Customer.objects.filter(
            company=company_id, is_available=True).order_by('id')
        return queryset
        # try:
        #     if not queryset.exists():
        #         raise Http404("Customers not found")
        #     return queryset
        # except Customer.DoesNotExist:
        #     raise Http404("Customers not found")


class RetrieveSuppliers(ListAPIView):
    permission_classes = [IsVendor]
    serializer_class = SupplierListSerializer

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = Supplier.objects.filter(
            company=company_id, is_available=True).order_by('id')
        return queryset
        # try:
        #     if not queryset.exists():
        #         raise Http404("Suppliers not found")
        #     return queryset
        # except Supplier.DoesNotExist:
        #     raise Http404("Suppliers not found")


class RetrieveDailyRegisters(ListAPIView):
    permission_classes = [IsVendor]
    serializer_class = DailyRegisterListSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = DailyRegister.objects.filter(company=company_id)
        try:
            if not queryset.exists():
                raise Http404("Daily register not found")
            return queryset
        except DailyRegister.DoesNotExist:
            raise Http404("Daily register not found")


class RetrieveQuotations(ListAPIView):
    permission_classes = [IsVendor]
    serializer_class = QuotationItemListSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = QuotationItems.objects.filter(quotation__company=company_id)
        try:
            if not queryset.exists():
                raise Http404("Quotations not found")
            return queryset
        except QuotationItems.DoesNotExist:
            raise Http404("Quotations not found")


class RetrievePurchases(ListAPIView):
    permission_classes = [IsVendor]
    serializer_class = PurchaseListSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = Purchase.objects.filter(company=company_id)
        try:
            if not queryset.exists():
                raise Http404("Purchases not found")
            return queryset
        except Purchase.DoesNotExist:
            raise Http404("Purchases not found")


class RetrieveExpenses(ListAPIView):
    permission_classes = [IsVendor]
    serializer_class = ExpenseListSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = Expense.objects.filter(company=company_id)
        try:
            if not queryset.exists():
                raise Http404("Expense not found")
            return queryset
        except Expense.DoesNotExist:
            raise Http404("Expenses not found")


class RetrieveStatementsOfAccounts(ListAPIView):
    permission_classes = [IsVendor]
    serializer_class = InvoiceListSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = StatementOfAccounts.objects.filter(company=company_id)
        try:
            if not queryset.exists():
                raise Http404("Invoice not found")
            return queryset
        except StatementOfAccounts.DoesNotExist:
            raise Http404("Invoice not found")


class RetrievePaymentCollections(ListAPIView):
    permission_classes = [IsVendor]
    serializer_class = PaymentCollectionListSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        queryset = PaymentCollections.objects.filter(company=company_id)
        try:
            if not queryset.exists():
                raise Http404("payment collections not found")
            return queryset
        except PaymentCollections.DoesNotExist:
            raise Http404("payment collections not found")
