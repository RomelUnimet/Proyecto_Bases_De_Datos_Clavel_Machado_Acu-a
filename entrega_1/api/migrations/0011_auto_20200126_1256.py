# Generated by Django 3.0.2 on 2020-01-26 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200126_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.ForeignKey(default='Hombre', on_delete=django.db.models.deletion.CASCADE, to='api.Genero'),
        ),
    ]
