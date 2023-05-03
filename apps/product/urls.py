from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include


router = DefaultRouter()
# router.register('resume', views.ResumeViewSet, basename='resume')
# router.register('vacancy', views.VacancyViewSet, basename='vacancy')

urlpatterns = [
    path('recommendation/', views.RecommendationView.as_view(), name='recommends'),
    path('vacancies/', views.VacancyListAPIView.as_view(), name='vacancy-list'),
    path('vacancies/<int:id>/', views.VacancyDetailAPIView.as_view(), name='vacancy-detail'),
    path('vacancies/update/<int:id>', views.VacancyUpdateAPIView.as_view(), name='vacancy-update'),
    path('vacancies/delete/<int:id>', views.VacancyDeleteAPIView.as_view(), name='vacancy-delete'),
    path('resume/', views.ResumeListAPIView.as_view(), name='resume'),
    path('resume/<int:id>/', views.ResumeDetailAPIView.as_view(), name='resume-detail'),
    path('resume/update/<int:pk>', views.ResumeUpdateAPIView.as_view(), name='resume-update'),
    path('resume/delete/<int:pk>', views.ResumeDeleteAPIView.as_view(), name='resume-delete'),
    path('companies/', views.CompanyListAPIView.as_view(), name='companies-list'),


    path('', include(router.urls)),

]
