# Generated by Django 4.2 on 2023-05-02 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
        ('feedback', '0010_remove_like_user_remove_like_vacancy_and_more'),
        ('product', '0010_remove_companyindustrysubtype_company_subtype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyindustry',
            name='company',
        ),
        migrations.RemoveField(
            model_name='companyindustrysubtype',
            name='industry_type',
        ),
        migrations.RemoveField(
            model_name='companyindustrytype',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='specializationsubtype',
            name='specialization_type',
        ),
        migrations.RemoveField(
            model_name='specializationtype',
            name='specialization',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='email',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='type_of_employment',
        ),
        migrations.AddField(
            model_name='resume',
            name='city',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='employment',
            field=models.CharField(choices=[('full-time', 'полная занятость'), ('part-time', 'частичная занятость'), ('temporary', 'временная занятость'), ('volunteer', 'волонтерство'), ('internship', 'стажировка'), ('freelance', 'фриланс'), ('entrepreneurship', 'предпринимательство')], default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='employment_at_company',
            field=models.ManyToManyField(blank=True, to='catalog.employmentatcompany'),
        ),
        migrations.AddField(
            model_name='resume',
            name='is_looking_for_job',
            field=models.CharField(blank=True, choices=[('yes', 'Да, я ищу работу'), ('no', 'Нет, я не ищу работу'), ('considering', 'Рассматриваю варианты')], max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='knowledge_of_languages',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='knowledge_of_languages', to='catalog.language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='location',
            field=location_field.models.plain.PlainLocationField(default=1, max_length=63),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='place_of_work',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='place_of_work', to='catalog.specializationsubtype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='schedule',
            field=models.CharField(choices=[('full-day', 'полный день'), ('part-day', 'неполный день'), ('shift-work', 'сменный график'), ('flexible-schedule', 'гибкий график'), ('remote-work', 'удаленная работа'), ('night-shift', 'ночная смена')], default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='specialization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='resume_specializations', to='catalog.specializationsubtype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='title',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='work_experience',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='employment',
            field=models.CharField(choices=[('full-time', 'полная занятость'), ('part-time', 'частичная занятость'), ('temporary', 'временная занятость'), ('volunteer', 'волонтерство'), ('internship', 'стажировка'), ('freelance', 'фриланс'), ('entrepreneurship', 'предпринимательство')], default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='knowledge_of_languages',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_languages', to='catalog.language'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='resume',
            name='experience',
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_skills', to='catalog.skill'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='catalog.company'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specializations', to='catalog.specializationsubtype'),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='CompanyIndustry',
        ),
        migrations.DeleteModel(
            name='CompanyIndustrySubType',
        ),
        migrations.DeleteModel(
            name='CompanyIndustryType',
        ),
        migrations.DeleteModel(
            name='Specialization',
        ),
        migrations.DeleteModel(
            name='SpecializationSubType',
        ),
        migrations.DeleteModel(
            name='SpecializationType',
        ),
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.ManyToManyField(blank=True, to='catalog.experience'),
        ),
    ]
