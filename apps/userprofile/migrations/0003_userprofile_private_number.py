# Generated by Django 4.2 on 2023-04-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_private_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='private_number',
            field=models.BooleanField(default=True),
        ),
    ]