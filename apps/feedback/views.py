from django.shortcuts import render
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from apps.feedback.mixins import LikeMixin, FavoriteMixin, VacancyUnwantedMixin, CompanyUnwantedMixin, SubscriptionMixin
from apps.feedback.models import Like, Favorite, VacancyUnwanted, CompanyUnwanted, Subscription, Comment
from apps.feedback.permissions import IsFavoriteOwner
from apps.feedback.serializers import LikeSerializer, FavoriteSerializer, UnwantedSerializer, CompanyUnwantedSerializer, \
    SubscriptionSerializer, CommentSerializer


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


class UnwantedAPIView(mixins.ListModelMixin, VacancyUnwantedMixin, GenericViewSet):
    queryset = VacancyUnwanted.objects.all()
    serializer_class = UnwantedSerializer
    permission_classes = [IsFavoriteOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CompanyUnwantedAPIView(mixins.ListModelMixin, CompanyUnwantedMixin, GenericViewSet):
    queryset = CompanyUnwanted.objects.all()
    serializer_class = CompanyUnwantedSerializer
    permission_classes = [IsFavoriteOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class SubscriptionAPIView(mixins.ListModelMixin, SubscriptionMixin, GenericViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsFavoriteOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsFavoriteOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)