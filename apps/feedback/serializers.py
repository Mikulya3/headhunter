from rest_framework import serializers

from apps.feedback.models import Favorite, VacancyUnwanted, Like


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

