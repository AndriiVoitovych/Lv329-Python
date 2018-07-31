from django.db import models

class Car(models.Model):
    DIESEL = 'D'
    PETROL = 'P'
    LPG = 'L'

    SELECT_THE_PETROL_CHOICES = (
        (DIESEL, 'Diesel'),
        (PETROL, 'Petrol'),
        (LPG, 'LPG'),
    )
    select_the_petrol = models.CharField(
        max_length = 1,
        choices = SELECT_THE_PETROL_CHOICES,
        default = DIESEL,
    )


    brand = models.CharField(max_length = 200)
    model = models.CharField(max_length = 200)
    product_year = models.DateField('date published')

    def __str__(self):
        return self.brand, self.model


class Mileage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    distance = models.IntegerField(default=0)
    mileage_data = models.DateField(default=0)
