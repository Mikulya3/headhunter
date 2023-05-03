from rest_framework import serializers

from apps.catalog.models import Company, LanguageLevel, Language, LanguageSkill, Education
from apps.product.models import Resume, Vacancy


class ResumeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

    class Meta:
        model = Resume
        fields = ('first_name', 'last_name', 'birthday', 'email', 'phone',
                  'summary', 'skills', 'experience', 'education', 'created_at', 'updated_at')


class LanguageSkillSerializer(serializers.ModelSerializer):
    language = serializers.CharField(source='language.language')
    level = serializers.CharField(source='level.name')

    class Meta:
        model = LanguageSkill
        fields = ('language', 'level')


class EducationSerializer(serializers.ModelSerializer):
    specialization = serializers.CharField(source='specialization.name')
    institute = serializers.CharField(source='institute.name')

    class Meta:
        model = Education
        fields = ('degree', 'year', 'specialization', 'institute')


class ResumeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ('title', 'work_experience', 'experience', 'employment_at_company', 'updated_at')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.is_looking_for_job is not None:
            ret['is_looking_for_job'] = instance.get_is_looking_for_job_display()
        else:
            del ret['is_looking_for_job']
        return ret


class ResumeDetailSerializer(serializers.ModelSerializer):
    specialization = serializers.CharField(source='specialization.name')
    skills = serializers.SerializerMethodField()
    knowledge_of_languages = LanguageSkillSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = ('gender', 'city', 'birthday', 'title', 'specialization', 'employment', 'schedule', 'work_experience',
                  'skills', 'education', 'knowledge_of_languages')

    def get_skills(self, obj):
        return list(obj.skills.values_list('title', flat=True))


class ResumeUpdateSerializer(serializers.ModelSerializer):
    specialization = serializers.CharField(source='specialization.name')
    skills = serializers.SerializerMethodField()
    knowledge_of_languages = LanguageSkillSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = '__all__'

    def get_skills(self, obj):
        return list(obj.skills.values_list('title', flat=True))


class VacancySerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name')

    class Meta:
        model = Vacancy
        fields = ('title', 'company', 'city', 'created_at')


class VacancyDetailSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name')
    skills = serializers.SerializerMethodField()
    knowledge_of_languages = LanguageSkillSerializer(many=True, read_only=True)
    specialization = serializers.CharField(source='specialization.name')

    class Meta:
        model = Vacancy
        fields = ('title', 'company', 'description', 'requirements', 'responsibilities', 'salary',
                  'required_experience', 'contact_information', 'city', 'location', 'employment', 'specialization',
                  'knowledge_of_languages', 'necessary_skills', 'skills', 'what_do_we_offer',
                  'created_at', 'updated_at')

    def get_skills(self, obj):
        return list(obj.skills.values_list('title', flat=True))


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('name', 'logo', 'description', 'location', 'website')


