from django.contrib import admin

from apps.product.models import Resume, Job

# Register your models here.

admin.site.register(Resume)
admin.site.register(Job)