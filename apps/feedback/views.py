from django.shortcuts import render
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from apps.feedback.mixins import LikeMixin, FavoriteMixin, \
    SubscriptionMixin, ReviewsMixin, UnwantedVacancyMixin, UnwantedCompanyMixin, FavoriteSpecializationMixin
from apps.feedback.models import Like, Favorite, UnwantedCompany, UnwantedVacancy, Subscription, Review, \
    FavoriteSpecialization
from apps.feedback.permissions import IsFavoriteOwner
from apps.feedback.serializers import LikeSerializer, FavoriteSerializer, UnwantedSerializer, CompanyUnwantedSerializer, \
    SubscriptionSerializer, ReviewSerializer, FavoriteSpecializationSerializer


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


class FavoriteSpecializationAPIView(mixins.ListModelMixin, FavoriteSpecializationMixin, GenericViewSet):
    queryset = FavoriteSpecialization.objects.all()
    serializer_class = FavoriteSpecializationSerializer
    permission_classes = [IsFavoriteOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class UnwantedAPIView(mixins.ListModelMixin, UnwantedVacancyMixin, GenericViewSet):
    queryset = UnwantedVacancy.objects.all()
    serializer_class = UnwantedSerializer
    permission_classes = [IsFavoriteOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CompanyUnwantedAPIView(mixins.ListModelMixin, UnwantedCompanyMixin, GenericViewSet):
    queryset = UnwantedCompany.objects.all()
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


class ReviewAPIView(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                    ReviewsMixin, GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset