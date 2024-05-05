from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from .search_views import *
router = DefaultRouter()
router.register(r'customer_search', CustomerSearch, basename='customer-search')
router.register(r'expense_search', ExpenseSearch, basename='expense-search')
router.register(r'supplier_search', SupplierSearch, basename='supplier-search')
router.register(r'purchase_search', PurchaseSearch, basename='purchase-search')
router.register(r'invoice_search', InvoiceSearch, basename='invoice-search')
router.register(r'daily_register_search', DailyRegisterSearch,
                basename='daily-register-search')
router.register(r'quotations_search', QuotationsSearch,
                basename='quotation-search')
router.register(r'payment_collection_search', PaymentCollectionSearch,
                basename='payment-collection-search')

urlpatterns = [
    path('customer_add/', CustomerAdd.as_view(), name='CustomerAdd'),
    path('customer_edit/<int:pk>/', CustomerEdit.as_view(), name='CustomerEdit'),

    path('supplier_add/', SupplierAdd.as_view(), name='SupplierAdd'),
    path('supplier_edit/<int:pk>/', SupplierEdit.as_view(), name='SupplierEdit'),

    path('daily_register_add/', DailyRegisterAdd.as_view(),
         name='Daily register creation'),
    path('daily_register_edit/<int:pk>/', DailyRegisterEdit.as_view(),
         name='Daily register editing and individual retrieval'),
    path('retrieve_next _order_id/<int:company_id>/', retrieve_last_order_id.as_view(),
         name='retrieve last order to create new order id'),

    path('quotation_add/', QuotationAdd.as_view(), name='Quotations creation'),
    path('quotation_edit/<int:pk>/', QuotationEdit.as_view(),
         name='Quotations Editing and individual retrieval'),

    path('quotation_items_add/', QuotationItemAdd.as_view(),
         name='Quotations items creation creation'),
    path('quotation_items_edit/<int:pk>/',
         QuotationItemEdit.as_view(), name='Quotations items edit'),

    path('retrieve_next_quotation_id/<int:company_id>/',
         retrieve_last_quotation_id.as_view(), name='Retrieving last quotation identifier'),

    path('purchase_add/', PurchaseAdd.as_view(), name='purchase creation'),
    path('purchase_edit/<int:pk>/', PurchaseEdit.as_view(),
         name='purchase edit and retrieval'),

    path('expense_add/', ExpenseAdd.as_view(), name='expense creation'),
    path('expense_edit/<int:pk>/', ExpenseEdit.as_view(),
         name='expense edit and retrieval'),

    path('invoice_add/', InvoiceAdd.as_view(), name='invoice creation'),
    path('invoice_edit/<int:pk>/', InvoiceEdit.as_view(),
         name='invoice edit and retrieval'),
    path('retrieve_next_invoice_id/<int:company_id>/',
         retrieve_invoice_id.as_view(), name='retrieving next id to set inv id'),

    path('payment_collection_add/', PaymentCollectionAdd.as_view(),
         name='payment collection creation'),
    path('payment_collection_edit/<int:pk>/', PaymentCollectionEdit.as_view(),
         name='payment collection edit and retrieval'),
    # List Api views
    path('retrieve_customers/<int:company_id>/',
         RetrieveCustomers.as_view(), name='Customers Retrieval'),
    path('retrieve_suppliers/<int:company_id>/',
         RetrieveSuppliers.as_view(), name='Suppliers Retrieval'),
    path('retrieve_daily_register/<int:company_id>/',
         RetrieveDailyRegisters.as_view(), name='Daily register retrieval'),
    path('retrieve_quotations/<int:company_id>/',
         RetrieveQuotations.as_view(), name='Quotation retrieval'),
    path('retrieve_purchases/<int:company_id>/',
         RetrievePurchases.as_view(), name='Purchases retrieval'),
    path('retrieve_expenses/<int:company_id>/',
         RetrieveExpenses.as_view(), name='Expenses retrieval'),
    path('retrieve_invoices/<int:company_id>/',
         RetrieveStatementsOfAccounts.as_view(), name='invoice retrieval'),
    path('retrieve_payment_collections/<int:company_id>/',
         RetrievePaymentCollections.as_view(), name='payment collections retrieval'),

    # search urls
    path('', include(router.urls)),
]
