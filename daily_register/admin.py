from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(DailyRegister)
admin.site.register(Quotation)
admin.site.register(QuotationItems)
admin.site.register(Purchase)
admin.site.register(Expense)
admin.site.register(StatementOfAccounts)
admin.site.register(PaymentCollections)
