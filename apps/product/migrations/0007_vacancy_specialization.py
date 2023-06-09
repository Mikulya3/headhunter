# Generated by Django 4.2 on 2023-04-28 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_specialization_specializationtype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='specialization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='specializations', to='product.specializationsubtype'),
            preserve_default=False,
        ),
    ]
