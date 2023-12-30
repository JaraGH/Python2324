from django.db import models

# Create your models here.


class UsedBikes(models.Model):
    bike_name = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    kms_driven = models.FloatField(blank=True, null=True)
    owner = models.TextField(blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    power = models.FloatField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Used_bikes'

