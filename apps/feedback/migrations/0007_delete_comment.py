# Generated by Django 4.2 on 2023-04-29 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_rename_reviews_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
