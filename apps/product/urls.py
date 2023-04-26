from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter
router.register('resume', views.ResumeViewSet, basename='resume')
router.register('', views.JobViewSet, basename='job')
