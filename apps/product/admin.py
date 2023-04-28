from django.contrib import admin

from apps.product.models import Resume, Vacancy, Company

# Register your models here.

admin.site.register(Resume)
admin.site.register(Vacancy)
admin.site.register(Company)