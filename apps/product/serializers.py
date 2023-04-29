from rest_framework import serializers

from apps.feedback.models import Like
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
                  'city', 'contact_information', 'specialization')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = Like.objects.filter(vacancy=instance, like=True).count()
        # reviews = Comment.objects.filter(vacancy=instance)
        # reviews = CommentSerializer(reviews, many=True).data
        # reviews = [{'user': i['user'], 'review': i['review']} for i in reviews]
        # rep['reviews'] = reviews
        return rep


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('name', 'logo', 'description', 'location', 'website')