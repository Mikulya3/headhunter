from rest_framework import serializers

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

    class Meta:
        model = Vacancy
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['name', 'logo', 'description', 'location', 'website']