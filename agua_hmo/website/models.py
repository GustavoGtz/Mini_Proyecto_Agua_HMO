from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

""" Everytime we made changes to the models, we need to update it. Use the next commands (In order):
    'python manage.py makemigrations'
    'python manage.py migrate'                                                                      """

MAX_CHAR_LENGTH = 20


# Create your models here.

class Users(models.Model):
    CONTRACT_TYPES = (
        ('R', 'Residencial'),
        ('C', 'Comercial'),
        ('I', 'Industrial'),
    )

    meter_number = models.IntegerField(validators=[
            MinValueValidator(10000, "El número debe ser mayor o igual a 10000."),
            MaxValueValidator(99999, "El número debe ser menor o igual a 99999.")
        ])
    user_name = models.CharField(max_length=MAX_CHAR_LENGTH)
    home_direction = models.CharField(max_length=MAX_CHAR_LENGTH)
    contract_type = models.CharField(max_length=MAX_CHAR_LENGTH)
    #register_date = models.DateField(max_length=1, choices=CONTRACT_TYPES)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.meter_number) + ' : ' + self.user_name

class Contracts(models.Model):
    ...

class Tickets(models.Model):

    meter_number = models.IntegerField(validators=[
        MinValueValidator(10000, "El número debe ser mayor o igual a 10000."),
        MaxValueValidator(99999, "El número debe ser menor o igual a 99999.")
    ])

    ticket_year = models.PositiveSmallIntegerField;
    ticket_month = models.PositiveSmallIntegerField;
    water_usage = models.FloatField(null=True)
