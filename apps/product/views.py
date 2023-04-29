from datetime import datetime, timedelta
from functools import reduce

import django_filters
from django.db.models import Q
from django.shortcuts import render
from django_filters import ModelMultipleChoiceFilter
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.feedback.models import Favorite, UnwantedCompany, UnwantedVacancy, FavoriteSpecialization
from apps.product.models import Resume, Vacancy,  SpecializationSubType, CompanyIndustrySubType
from apps.product.serializers import ResumeSerializer, VacancySerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100000


class SpecializationFilter(django_filters.FilterSet):

    subtype = ModelMultipleChoiceFilter(
        field_name='specialization_type__name',
        queryset=SpecializationSubType.objects.all(),
        to_field_name='name',
        label='Выберите специализацию'
    )

    company_subtype = ModelMultipleChoiceFilter(
        field_name='company_subtype__company_type__name__company__name',
        queryset=CompanyIndustrySubType.objects.all(),
        to_field_name='name',
        label='Отрасль Компании'
    )

    class Meta:
        model = Vacancy
        fields = ['subtype', 'company', 'company_subtype']


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_class = SpecializationFilter
    # filterset_fields = ['specialization', ]
    pagination_class = LargeResultsSetPagination
    search_fields = ['title', 'company__name', 'description']


class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecommendationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        latest_vacancies = Vacancy.objects.filter(created_at__gte=datetime.now()-timedelta(days=180)
                                                  ).order_by('-created_at')[:5]
        if len(latest_vacancies) < 10:
            latest_vacancies = Vacancy.objects.filter(created_at__gte=datetime.now()-timedelta(days=180))

        favorite_specializations = FavoriteSpecialization.objects.filter(user=user).values_list('specialization',
                                                                                                flat=True)

        favorite_vacancies = Favorite.objects.filter(user=user).values_list('vacancy', flat=True)

        unwanted_companies = UnwantedCompany.objects.filter(user=user).values_list('company', flat=True)

        unwanted_vacancies = UnwantedVacancy.objects.filter(user=user).values_list('vacancy', flat=True)

        if favorite_specializations:
            vacancy_list = Vacancy.objects.filter(reduce(lambda x, y: x | y,
                                                         [Q(specialization=specialization)
                                                          for specialization in favorite_specializations]))
        else:
            vacancy_list = Vacancy.objects.all()

        if unwanted_vacancies:
            vacancy_list = vacancy_list.exclude(id__in=unwanted_vacancies)

        if unwanted_companies:
            vacancy_list = vacancy_list.exclude(reduce(lambda x, y: x | y, [Q(company=company)
                                                                            for company in unwanted_companies]))

        vacancy_list = vacancy_list.order_by('-created_at')

        if len(vacancy_list) < 10:
            serializer = VacancySerializer(vacancy_list, many=True)
            return Response(serializer.data)

        vacancy_list = sorted(vacancy_list, key=lambda v: len(set(v.specialization.all()) &
                                                              set(favorite_specializations)), reverse=True)
        recommend_vacancies = vacancy_list[:10]

        serializer = VacancySerializer(recommend_vacancies, many=True)
        return Response(serializer.data)