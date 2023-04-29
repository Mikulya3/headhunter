from django.db.models import Avg
from rest_framework import serializers

from apps.feedback.models import Like, Review
from apps.feedback.serializers import ReviewSerializer
from apps.product.models import Resume, Vacancy, Company


class ResumeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

    class Meta:
        model = Resume
        fields = ('first_name', 'last_name', 'birthday', 'email', 'phone',
                  'summary', 'skills', 'experience', 'education', 'created_at', 'updated_at')


class VacancySerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name')
    specialization = serializers.CharField(source='specialization.name')

    class Meta:
        model = Vacancy
        fields = ('company', 'title', 'description', 'salary', 'location',
                  'city', 'contact_information', 'specialization', 'type_of_employment')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = Like.objects.filter(vacancy=instance, like=True).count()
        reviews = Review.objects.filter(vacancy=instance)
        reviews = ReviewSerializer(reviews, many=True).data
        reviews = [{'user': i['user'], 'rating': i['rating'], 'text': i['text']} for i in reviews]
        rep['reviews'] = reviews
        rating = Review.objects.filter(vacancy=instance).aggregate(Avg('rating'))['rating__avg']
        if rating:
            rep['rating'] = rating
        else:
            rep['rating'] = 0
        return rep


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('name', 'logo', 'description', 'location', 'website')