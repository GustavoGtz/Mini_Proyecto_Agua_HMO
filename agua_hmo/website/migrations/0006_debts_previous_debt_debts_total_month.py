# Generated by Django 4.2.5 on 2023-09-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_debts_debt'),
    ]

    operations = [
        migrations.AddField(
            model_name='debts',
            name='previous_debt',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='debts',
            name='total_month',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
