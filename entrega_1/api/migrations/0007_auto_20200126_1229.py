# Generated by Django 3.0.2 on 2020-01-26 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_employee_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.ForeignKey(default='Hombre', on_delete=django.db.models.deletion.CASCADE, to='api.Genero'),
        ),
    ]
