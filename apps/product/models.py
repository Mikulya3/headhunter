from django.contrib.auth import get_user_model
from django.db import models
from birthday import BirthdayField
from location_field.models.plain import PlainLocationField

# Create your models here.
User = get_user_model()


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthday = BirthdayField()
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    summary = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    keywords = models.TextField()

    def __str__(self):
        return self.name


class SpecializationType(models.Model):
    name = models.CharField(max_length=128)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='sp_types')
    description = models.TextField()
    keywords = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.specialization.name})'


class SpecializationSubType(models.Model):
    name = models.CharField(max_length=128)
    specialization_type = models.ForeignKey(SpecializationType, on_delete=models.CASCADE, related_name='sps_type')
    description = models.TextField()
    keywords = models.TextField()

    def __str__(self):
        return f'{self.name}: {self.specialization_type.name} ({self.specialization_type.specialization.name})'


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companies')
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    contact_information = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    specialization = models.ForeignKey(SpecializationSubType, on_delete=models.CASCADE, related_name='specializations')
    type_of_employment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title


class CompanyIndustry(models.Model):
    name = models.CharField(max_length=128)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='industries')

    def __str__(self):
        return self.name


class CompanyIndustryType(models.Model):
    name = models.CharField(max_length=128)
    industry = models.ForeignKey(CompanyIndustry, on_delete=models.CASCADE, related_name='types')

    def __str__(self):
        return f'{self.name}: {self.industry.name}'


class CompanyIndustrySubType(models.Model):
    name = models.CharField(max_length=128)
    industry_type = models.ForeignKey(CompanyIndustryType, on_delete=models.CASCADE, related_name='subtypes')

    def __str__(self):
        return f'{self.name}: {self.industry_type.name} ({self.industry_type.industry.name})'




