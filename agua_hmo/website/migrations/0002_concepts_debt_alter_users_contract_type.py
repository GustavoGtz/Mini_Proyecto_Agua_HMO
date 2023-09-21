# Generated by Django 4.2.5 on 2023-09-21 01:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concepts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('consumption_per_cubic', models.DecimalField(decimal_places=2, max_digits=10)),
                ('drainage_fee', models.DecimalField(decimal_places=2, max_digits=3)),
                ('sanitation', models.DecimalField(decimal_places=2, max_digits=3)),
                ('red_cross', models.DecimalField(decimal_places=2, max_digits=3)),
                ('firefighters', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(10000, 'El número debe ser mayor o igual a 10000.'), django.core.validators.MaxValueValidator(99999, 'El número debe ser menor o igual a 99999.')])),
                ('water_usage', models.FloatField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='contract_type',
            field=models.DateField(choices=[('R', 'Residencial'), ('C', 'Comercial'), ('I', 'Industrial')], max_length=1),
        ),
    ]