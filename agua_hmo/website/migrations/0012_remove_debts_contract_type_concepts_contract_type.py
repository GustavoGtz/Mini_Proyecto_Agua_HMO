# Generated by Django 4.2 on 2023-09-24 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0011_debts_contract_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="debts",
            name="contract_type",
        ),
        migrations.AddField(
            model_name="concepts",
            name="contract_type",
            field=models.CharField(
                choices=[
                    ("Residencial", "RESIDENCIAL"),
                    ("Comercial", "COMERCIAL"),
                    ("Industrial", "INDUSTRIAL"),
                ],
                default="RESIDENCIAL",
                max_length=12,
            ),
            preserve_default=False,
        ),
    ]