from django.db import models
from vendors.models import CompanyProfile
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# Create your models here.


class Customer(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30)
    contact_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(default="")
    country = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    tax_number = models.CharField(max_length=50, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.customer_name

    class Meta:
        unique_together = ('company', 'customer_name')


class Supplier(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=30)
    contact_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(default="")
    country = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    tax_number = models.CharField(max_length=50, blank=True, null=True)
    item_name = models.CharField(max_length=20)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.supplier_name

    class Meta:
        unique_together = ('company', 'supplier_name', 'item_name')


class DailyRegister(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=True)
    order_id = models.CharField(max_length=10, db_index=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    client = models.CharField(max_length=20)
    contact_number = PhoneNumberField(blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)

    work_type = models.CharField(max_length=15)
    project_name = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    landmark = models.CharField(max_length=50, blank=True, null=True)
    nature_of_work = models.CharField(max_length=15)
    building_name = models.CharField(max_length=20, blank=True, null=True)
    villa_number = models.IntegerField(blank=True, null=True)
    quoted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00)
    vat_or_tax = models.CharField(max_length=50, blank=True, null=True)
    final_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    payment_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    balance_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    payment_date = models.DateField()
    payment_type = models.CharField(max_length=20)
    payment_remarks = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.order_date} - Order {self.order_id}"

    class Meta:
        unique_together = ('company', 'order_id')


class Quotation(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    quotation_identifier = models.CharField(max_length=10, db_index=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_terms = models.TextField()
    requirements = models.TextField()
    pricing = models.TextField()
    other_terms = models.TextField()
    is_available = models.BooleanField(default=True)
    quotation_date = models.DateField(auto_now=True)
    quotation_status = models.CharField(max_length=20, default='Pending')

    def __str__(self) -> str:
        return f"{self.quotation_identifier} to {self.customer.customer_name}"

    class Meta:
        unique_together = ('company', 'quotation_identifier')


class QuotationItems(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    discount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    vat_or_tax = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.quotation.quotation_identifier} items are {self.description}"

    class Meta:
        unique_together = ('quotation', 'description')


class Purchase(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item_purchase = models.CharField(max_length=20)
    vat_or_tax = models.CharField(max_length=20, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=12, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=30)
    purchase_against = models.ForeignKey(
        DailyRegister, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    purchase_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.supplier.supplier_name} purchased happened on {self.purchase_against.order_id}"

    class Meta:
        unique_together = ('company', 'supplier', 'item_purchase',
                           'bill_amount', 'payment_type', 'purchase_against')


class Expense(models.Model):
    company = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE, default='')
    to = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=20)
    expense_against = models.ForeignKey(
        DailyRegister, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.to.customer_name} expenses charges on {self.expense_against.order_id}"

    class Meta:
        unique_together = ('to', 'description', 'amount_paid', 'company',
                           'payment_type', 'expense_against')


class StatementOfAccounts(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    invoice_identifier = models.CharField(max_length=10, db_index=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.ForeignKey(DailyRegister, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    invoice_amount = models.DecimalField(max_digits=12, decimal_places=2)
    invoice_status = models.CharField(max_length=20, default="Pending")
    is_available = models.BooleanField(default=True)
    invoice_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.invoice_identifier} issued to {self.customer.customer_name}"

    class Meta:
        unique_together = ('company', 'order_id', 'customer')


class PaymentCollections(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    payment_type = models.CharField(max_length=20)
    cheque_number = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=25, blank=True, null=True)
    collection_date = models.DateField()
    invoice = models.ForeignKey(StatementOfAccounts, on_delete=models.CASCADE)
    invoice_amount = models.DecimalField(max_digits=12, decimal_places=2)
    differences = models.DecimalField(max_digits=12, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.customer.customer_name} payment  {self.invoice.invoice_identifier}"

    class Meta:
        unique_together = ('company', 'invoice', 'customer')
