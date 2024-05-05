from rest_framework.serializers import ModelSerializer
from userside.serializers import *
from .models import *
from users.serializers import userDataSerializer
from vendors.serializers import CompanyJobsListSerializer


class JobApplicationSerializer(ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"


class JobApplicationListSerializer(ModelSerializer):
    user = userDataSerializer()
    jobs = CompanyJobsListSerializer()

    class Meta:
        model = JobApplication
        fields = "__all__"