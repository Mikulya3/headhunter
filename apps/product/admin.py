from django.contrib import admin

from apps.product.models import Resume, Vacancy, Company, Specialization,\
    SpecializationType, SpecializationSubType, CompanyIndustryType, CompanyIndustry, CompanyIndustrySubType

# Register your models here.

admin.site.register(Resume)
admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Specialization)
admin.site.register(SpecializationType)
admin.site.register(SpecializationSubType)
admin.site.register(CompanyIndustry)
admin.site.register(CompanyIndustryType)
admin.site.register(CompanyIndustrySubType)