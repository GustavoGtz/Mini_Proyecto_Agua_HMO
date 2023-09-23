from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

""" Everytime we made changes to the models, we need to update it. Use the next commands (In order):
    'python manage.py makemigrations'
    'python manage.py migrate'                                                                      """

MAX_CHAR_LENGTH = 20


# Create your models here.

class Users(models.Model):
    CONTRACT_TYPES = (
        ('Residencial', 'RESIDENCIAL'),
        ('Comercial', 'COMERCIAL'),
        ('Industrial', 'INDUSTRIAL'),
    )
    
    meter_number = models.IntegerField(validators=[
            MinValueValidator(10000, "El número debe ser mayor o igual a 10000."),
            MaxValueValidator(99999, "El número debe ser menor o igual a 99999.")
        ], unique=True)
    user_name = models.CharField(max_length=MAX_CHAR_LENGTH)
    home_direction = models.CharField(max_length=MAX_CHAR_LENGTH)
    contract_type = models.CharField(max_length=12, choices=CONTRACT_TYPES)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.meter_number) + ' : ' + self.user_name

class Concepts(models.Model):
    year = models.DecimalField(max_digits=4, decimal_places=0)
    consumption_per_cubic = models.FloatField()
    drainage_fee = models.FloatField()
    sanitation = models.FloatField()
    red_cross = models.FloatField()
    firefighters = models.FloatField()
    
    def __str__(self):
        return str(self.year)

class Debts(models.Model):
    meter_number = models.IntegerField(validators=[
        MinValueValidator(10000, "El número debe ser mayor o igual a 10000."),
        MaxValueValidator(99999, "El número debe ser menor o igual a 99999.")
    ])

    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    cut = models.PositiveSmallIntegerField()
    water_usage_m3 = models.FloatField()
    previous_debt = models.FloatField()
    total_month = models.FloatField()

    def __str__(self):
        return str(self.meter_number) + " : " + str(self.year) + "-" + str(self.month)


