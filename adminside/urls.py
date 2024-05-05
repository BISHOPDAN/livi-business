from django.urls import path
from .views import *

urlpatterns = [
    # notification management
    path("vendor_notification_retrieve/", RetrieveVendorNotification.as_view(),
         name="vendor_notification_retrieve",),
    path("vendor_notification_edit/<int:pk>/",
         VendorNotificationEdit.as_view(), name="vendor_notification_edit",),
    #  user management
    path('all_user_listing/', RetrieveAllUsers.as_view(), name="all_users_listing"),
    path('all_vendor_listing/', RetrieveAllVendors.as_view(),
         name="all_vendors_listing"),
    path('user_block_and_unblock/<int:user_id>/',
         BlockAndUnBlockUser.as_view(), name="user_block_and_unblock"),
    path('vendor_block_and_unblock/<int:company_id>/',
         BlockAndUnBlockVendor.as_view(), name="user_block_and_unblock")
]
