# Generated by Django 4.2 on 2023-04-28 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_company_city_vacancy_city_alter_company_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='email',
        ),
    ]