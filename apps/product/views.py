import django_filters
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from apps.product.models import Resume, Company, Vacancy, Specialization, SpecializationSubType
from apps.product.serializers import ResumeSerializer, VacancySerializer, CompanySerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100000


class SpecializationFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(field_name='specializationtype__name')
    subtype = django_filters.CharFilter(field_name='specializationtype__specializationsubtype__name')

    class Meta:
        model = Specialization
        fields = ['subtype', 'type']


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    # filterset_class = SpecializationFilter
    pagination_class = LargeResultsSetPagination
    search_fields = ['title']


class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]


