from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register('resume', views.ResumeViewSet, basename='resume')
router.register('job', views.VacancyViewSet, basename='vacancy')

urlpatterns = [
    path('', include(router.urls)),
]
