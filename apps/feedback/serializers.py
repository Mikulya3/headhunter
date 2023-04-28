from rest_framework import serializers

from apps.feedback.models import Favorite, VacancyUnwanted, Like, CompanyUnwanted, Subscription, Comment


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = instance.user.email
        rep['vacancy'] = instance.vacancy.title
        return rep


class UnwantedSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyUnwanted
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = instance.user.first_name
        rep['vacancy'] = instance.vacancy.title


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['vacancy'] = instance.vacancy.title
        return rep


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['company'] = instance.company.name
        return rep


class CompanyUnwantedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyUnwanted
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['company'] = instance.company.name
        return rep


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['vacancy'] = instance.vacancy.title
        return rep

