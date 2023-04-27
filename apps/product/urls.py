from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

router = DefaultRouter()
router.register('resume', views.ResumeViewSet, basename='resume')
router.register('', views.JobViewSet, basename='job')


urlpatterns = [
    path('', views.index, name='index'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('resume/<int:pk>/', views.resume_detail, name='resume_detail'),
    path('job_new/', views.job_new, name='job_new'),
    path('job_edit/<int:pk>/edit/', views.job_edit, name='job_edit'),
    path('resume_edit/<int:pk>/edit/', views.resume_edit, name='resume_edit'),
    path('job_delete/<int:pk>/', views.job_delete, name='job_delete'),
    # path('<int:pk>/like/', AddLike.as_view(), name='like'),
    # path('post/<int:pk>/', post_detail, name='post_detail'),
    # path('post_new/', post_new, name='post_new'),
    ]

