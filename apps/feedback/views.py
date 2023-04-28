from django.shortcuts import render
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from apps.feedback.mixins import LikeMixin, FavoriteMixin
from apps.feedback.models import Like, Favorite
from apps.feedback.permissions import IsFavoriteOwner
from apps.feedback.serializers import LikeSerializer, FavoriteSerializer


class LikeAPIView(mixins.ListModelMixin, LikeMixin, GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class FavoriteAPIView(mixins.ListModelMixin,  FavoriteMixin, GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsFavoriteOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

