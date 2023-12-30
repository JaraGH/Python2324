from django.db import models

# Create your models here.


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True, max_length=50)
    continent = models.TextField(blank=True, max_length=30)

    class Meta:
        managed = True
        db_table = 'worldcountries'

