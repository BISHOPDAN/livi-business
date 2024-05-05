from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from users.permissions import *

from .serializers import *

# Create your views here.

class JobApplicationCreate(generics.CreateAPIView):
    """
    Create job Application
    """
    permission_classes = (IsAuthenticated,)
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer



class JobApplicationList(generics.ListAPIView):
    """
    list all Job Application
    """
    permission_classes = (IsAuthenticated,)
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationListSerializer
    


class JobApplicationUpdate(generics.UpdateAPIView):
    """
    create job Application
    """
    permission_classes = (IsAuthenticated,)
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer



class JobApplicationRetrieve(generics.RetrieveAPIView):
    """
    Retrieve job Application
    """
    permission_classes = (IsAuthenticated,)
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
