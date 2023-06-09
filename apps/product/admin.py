from django.contrib import admin

from apps.catalog.models import Specialization, SpecializationType, SpecializationSubType, CompanyIndustry, \
    CompanyIndustryType, CompanyIndustrySubType, Language, LanguageLevel, LanguageSkill, Company, Skill, \
    EmploymentAtCompany, Experience, Education, Institute, NativeLanguage
from apps.product.models import Resume, Vacancy

# from apps.product.models import Resume, Vacancy, Company, Specialization, SpecializationType, SpecializationSubType, \
#     CompanyIndustry, CompanyIndustryType, CompanyIndustrySubType, Language, LanguageLevel, LanguageSkill, Skill, \
#     Experience, EmploymentAtCompany, Education, Institute, NativeLanguage

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
admin.site.register(Language)
admin.site.register(LanguageLevel)
admin.site.register(LanguageSkill)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(EmploymentAtCompany)
admin.site.register(Education)
admin.site.register(Institute)
admin.site.register(NativeLanguage)