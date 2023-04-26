from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path("register/", views.RegisterAPIView.as_view(), name='register'),
    path("confirm/<uuid:activation_code>/", views.ActivationAPIView.as_view()),

    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]