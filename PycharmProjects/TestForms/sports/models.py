from django.db import models

# Create your models here.

SPORT_TYPES = {
        "M": "Motor",
        "B": "Ball Sport",
        "W": "Water Sport",
        "A": "Air Sport",
        "K": "Bikes",
        "T": "Athletics",
    }


class Sport(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_outdoor = models.BooleanField(default=False, blank=True)
    number_players = models.IntegerField(default=0)
    type = models.CharField(max_length=1, choices=SPORT_TYPES)
    origin = models.CharField(max_length=50, default='Unknown')
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name + '-' + str(self.number_players)
