from rest_framework.serializers import ModelSerializer
from users.serializers import *
from vendors.serializers import VendorSerializer
from rest_framework import serializers
from .models import *


# Customer Serializer
class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"


class CustomerListSerializer(ModelSerializer):
    company = VendorSerializer()

    class Meta:
        model = Customer
        fields = "__all__"

# Supplier Serializer


class SupplierSerializer(ModelSerializer):

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierListSerializer(ModelSerializer):
    company = VendorSerializer()

    class Meta:
        model = Supplier
        fields = "__all__"

# Daily register serializer


class DailyRegisterSerializer(ModelSerializer):

    class Meta:
        model = DailyRegister
        fields = "__all__"


class DailyRegisterListSerializer(ModelSerializer):
    # company = VendorSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = DailyRegister
        fields = "__all__"


# Quotation and its items serializer

class QuotationSerializer(ModelSerializer):

    class Meta:
        model = Quotation
        fields = "__all__"


class QuotationListSerializer(ModelSerializer):
    company = VendorSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Quotation
        fields = "__all__"


class QuotationItemSerializer(ModelSerializer):

    class Meta:
        model = QuotationItems
        fields = "__all__"


class QuotationItemListSerializer(ModelSerializer):
    quotation = QuotationListSerializer()

    class Meta:
        model = QuotationItems
        fields = "__all__"

# Purchase Serializer


class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"


class PurchaseListSerializer(ModelSerializer):
    company = VendorSerializer()
    purchase_against = DailyRegisterSerializer()

    class Meta:
        model = Purchase
        fields = "__all__"

# expense serializer


class ExpenseSerializer(ModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__"


class ExpenseListSerializer(ModelSerializer):
    company = VendorSerializer()
    to = CustomerSerializer()
    expense_against = DailyRegisterSerializer()

    class Meta:
        model = Expense
        fields = "__all__"

# Statements of Accounts serializers


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = StatementOfAccounts
        fields = "__all__"


class InvoiceListSerializer(ModelSerializer):
    company = VendorSerializer()
    customer = CustomerSerializer()
    order_id = DailyRegisterSerializer()

    class Meta:
        model = StatementOfAccounts
        fields = "__all__"

# payment collection serializer


class PaymentCollectionSerializer(ModelSerializer):
    class Meta:
        model = PaymentCollections
        fields = "__all__"


class PaymentCollectionListSerializer(ModelSerializer):
    company = VendorSerializer()
    customer = CustomerSerializer()
    invoice = InvoiceSerializer()

    class Meta:
        model = PaymentCollections
        fields = "__all__"
