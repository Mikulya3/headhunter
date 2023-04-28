from django.contrib.auth import get_user_model
from django.db import models

from apps.product.models import Vacancy, Company

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f'{self.user}'


class VacancyUnwanted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vc_unwanted')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vc_unwanted')

    def __str__(self):
        return f'{self.user}'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='subscriptions')

    def __str__(self):
        return f'{self.user}'


class CompanyUnwanted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cm_unwanted')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='cm_unwanted')

    def __str__(self):
        return f'{self.user}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user}'
