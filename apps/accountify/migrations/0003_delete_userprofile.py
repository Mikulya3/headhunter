# Generated by Django 4.2 on 2023-04-26 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountify', '0002_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
