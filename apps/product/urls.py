from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register('resume', views.ResumeViewSet, basename='resume')
router.register('vacancy', views.VacancyViewSet, basename='vacancy')

urlpatterns = [
    path('recommended/', views.RecommendationView.as_view(), name='recommends'),
    path('', include(router.urls)),

]
