# Generated by Django 4.2 on 2023-04-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_vacancy_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='type_of_employment',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
