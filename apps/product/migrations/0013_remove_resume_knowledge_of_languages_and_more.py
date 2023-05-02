# Generated by Django 4.2 on 2023-05-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('product', '0012_remove_resume_skills_resume_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='knowledge_of_languages',
        ),
        migrations.AddField(
            model_name='resume',
            name='knowledge_of_languages',
            field=models.ManyToManyField(blank=True, to='catalog.language'),
        ),
    ]
