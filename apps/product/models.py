from django.contrib.auth import get_user_model
from django.db import models
from birthday import BirthdayField
from location_field.models.plain import PlainLocationField

from apps.catalog.models import SpecializationSubType, Skill, EmploymentAtCompany, Experience, Language, Company, \
    Education, LanguageSkill, NativeLanguage

# Create your models here.
User = get_user_model()


TypeofEmployment = (
    ('full-time', 'полная занятость'),
    ('part-time', 'частичная занятость'),
    ('temporary', 'временная занятость'),
    ('volunteer', 'волонтерство'),
    ('internship', 'стажировка'),
    ('freelance', 'фриланс'),
    ('entrepreneurship', 'предпринимательство')
)

SCHEDULE = (
    ('full-day', 'полный день'),
    ('part-day', 'неполный день'),
    ('shift-work', 'сменный график'),
    ('flexible-schedule', 'гибкий график'),
    ('remote-work', 'удаленная работа'),
    ('night-shift', 'ночная смена'),
)


IS_LOOKING_FOR_JOB_CHOICES = (
    ('yes', 'Да, я ищу работу'),
    ('no', 'Нет, я не ищу работу'),
    ('considering', 'Рассматриваю варианты'),
)

GENDER = (
    ('male', 'Мужской'),
    ('female', 'Женский')
)


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    specialization = models.ForeignKey(SpecializationSubType, on_delete=models.CASCADE,
                                       related_name='resume_specializations')
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    birthday = BirthdayField()
    phone = models.CharField(max_length=128)
    summary = models.TextField()
    skills = models.ManyToManyField(Skill, blank=True)
    place_of_work = models.ForeignKey(SpecializationSubType, on_delete=models.CASCADE, related_name='place_of_work')
    experience = models.ManyToManyField(Experience, blank=True)
    employment_at_company = models.ManyToManyField(EmploymentAtCompany, blank=True)
    employment = models.CharField(choices=TypeofEmployment, max_length=128)
    schedule = models.CharField(choices=SCHEDULE, max_length=128)
    work_experience = models.CharField(max_length=128)
    native_language = models.ForeignKey(NativeLanguage, on_delete=models.CASCADE, related_name='native_language')
    knowledge_of_languages = models.ManyToManyField(LanguageSkill, blank=True)
    is_looking_for_job = models.CharField(choices=IS_LOOKING_FOR_JOB_CHOICES, max_length=128, null=True, blank=True)
    gender = models.CharField(choices=GENDER, blank=True)
    about_me = models.TextField()
    education = models.ManyToManyField(Education, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companies')
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    salary = models.CharField(null=True, blank=True)
    contact_information = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    specialization = models.ForeignKey(SpecializationSubType, on_delete=models.CASCADE, related_name='specializations')
    employment = models.CharField(choices=TypeofEmployment, max_length=128)
    knowledge_of_languages = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='vacancy_languages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title







