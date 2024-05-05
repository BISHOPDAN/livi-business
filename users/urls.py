from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('token/', Login.as_view(), name='MyTokenObtainPairView'),
    path('signup/', Signup.as_view(), name='sign_up'),
    path('google_login/', Google_login.as_view(), name='Google_login'),
    path('otpverification/', OtpVerification.as_view(), name='otpverification'),
    path('forgotpassword/', ForgotPassword.as_view(), name='forgotpassword'),
    path('verifyforgotemail/', VerifyForgotEmail.as_view(),
         name='verifyforgotemail'),
    path('updatepassword/', UpdatePassword.as_view(), name='updatepassword'),

    # New URLs for Enquiry Adding If you dont need remove this and dont forget t remove the view also
    path('enquiry_add/', EnquiryAdd.as_view(), name='EnquiryAdd'),
    path('logout/',Logout.as_view(),name ='logout'),
    

]
