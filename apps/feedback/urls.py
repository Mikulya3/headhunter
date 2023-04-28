from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.feedback.views import LikeAPIView, FavoriteAPIView, UnwantedAPIView, CompanyUnwantedAPIView, \
    SubscriptionAPIView, CommentViewSet

router = DefaultRouter()
router.register('like', LikeAPIView)
router.register('favourite', FavoriteAPIView)
router.register('unwanted', UnwantedAPIView)
router.register('unwanted/company', CompanyUnwantedAPIView)
router.register('subscription', SubscriptionAPIView)
router.register('comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]