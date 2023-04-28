from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.feedback.views import LikeAPIView, FavoriteAPIView

router = DefaultRouter()
router.register('like', LikeAPIView)
router.register('favourite', FavoriteAPIView)

urlpatterns = [
    path('', include(router.urls))
]