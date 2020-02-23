# Generated by Django 3.0.2 on 2020-02-23 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Online', 'Online')], max_length=60)),
                ('currency', models.CharField(choices=[('Dolares', 'Dolares'), ('Bolivares', 'Bolivares'), ('Euros', 'Euros')], max_length=60)),
                ('total', models.FloatField()),
                ('account_n', models.BigIntegerField()),
                ('availible', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameField(
            model_name='delivery',
            old_name='manager',
            new_name='delivery_boy',
        ),
        migrations.RenameField(
            model_name='productbatch',
            old_name='quantity',
            new_name='actual_quantity',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='paument_method',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='total',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='max_time',
        ),
        migrations.AddField(
            model_name='client',
            name='zone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Zone'),
        ),
        migrations.AddField(
            model_name='currencyexchange',
            name='date',
            field=models.DateField(default='1999-03-12'),
        ),
        migrations.AddField(
            model_name='pickup',
            name='availible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productbatch',
            name='elaboration_date',
            field=models.DateField(default='1999-03-12'),
        ),
        migrations.AddField(
            model_name='productbatch',
            name='local',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Local'),
        ),
        migrations.AddField(
            model_name='productbatch',
            name='quantity_sold',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Otro', 'Otro')], max_length=60),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_id',
            field=models.CharField(choices=[('Gerente', 'Gerente'), ('Repartidor', 'Repartidor'), ('Cajero', 'Cajero')], max_length=60),
        ),
        migrations.AlterField(
            model_name='productbatch',
            name='expiration_date',
            field=models.DateField(default='1999-03-12'),
        ),
        migrations.CreateModel(
            name='Payment_Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availible', models.BooleanField(default=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Bill')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Payment')),
            ],
        ),
    ]
