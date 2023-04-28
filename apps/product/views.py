from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from apps.product.models import Resume, Company, Vacancy
from apps.product.permissions import ReadOnlyOrAdmin
from apps.product.serializers import ResumeSerializer, VacancySerializer, CompanySerializer


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticated]


class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]


