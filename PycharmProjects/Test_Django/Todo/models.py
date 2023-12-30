from django.db import models

from Todo.utils import image_upload_location

class Company(models.Model):
    name = models.CharField('name', max_length=50)
    tax_number = models.IntegerField('Tax number', unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']  ## -name DESC

    def __str__(self):
        return self.name

# definición de clase
class Beer(models.Model):

    COLOR_YELLOW, COLOR_BLACK, COLOR_AMBAR, COLOR_BROWN = [1,2,3,4]
    COLOR_CHOICES = {
        (1, "yellow"),
        (2, "black"),
        (3, "amber"),
        (4, "brown"),
    }

    name = models.CharField(name='Name', max_length=50)
    abv = models.DecimalField(name='Alcohol by volume', max_digits=5, decimal_places=2, default=4.8)
    is_filtered = models.BooleanField(name='Is filtered', default=False)
    color = models.PositiveSmallIntegerField('Color', choices=COLOR_CHOICES, default=COLOR_YELLOW)
    image = models.ImageField('Image', blank=True, null=True, upload_to=image_upload_location)
    company = models.ForeignKey (Company, related_name='beers', on_delete=models.R)

    class Meta:
        verbose_name = 'Beer'
        verbose_name_plural = 'Beers'
        ordering = ['name']  ## -name DESC

    def __str__(self):
        return self.name

class SpecialIngredient(models.Model):
    name = models.CharField(name='name', max_length=50)
    beers = models.ManyToManyField (Beer, blank=True, related_name="special_ingredients")

    class Meta:
        verbose_name = 'Special ingredient'
        verbose_name_plural = 'Special Ingredients'
        ordering = ['name']  ## -name DESC

    def __str__(self):
        return self.name
