from django.contrib import admin

from apps.feedback.models import Favorite, Like, VacancyUnwanted, CompanyUnwanted, Subscription

# Register your models here.

admin.site.register(Favorite)
admin.site.register(Like)
admin.site.register(VacancyUnwanted)
admin.site.register(CompanyUnwanted)
admin.site.register(Subscription)
