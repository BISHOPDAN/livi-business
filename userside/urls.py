from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import *


urlpatterns = [
    path('jobs/create/', JobApplicationCreate.as_view(), name='job_create'),
    path('jobs/list/', JobApplicationList.as_view(), name='job_list'),
    path('jobs/<int:pk>/update/', JobApplicationUpdate.as_view(), name='job_update'),
    path('jobs/retrieve/<int:pk>/', JobApplicationRetrieve.as_view(), name='job_retrieve'),
]
