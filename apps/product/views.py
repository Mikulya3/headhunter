from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from apps.accountify.models import Resume, Job
from apps.product.serializers import ResumeSerializer


# Create your views here.

class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = ResumeSerializer