# Generated by Django 3.0.2 on 2020-02-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200223_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
