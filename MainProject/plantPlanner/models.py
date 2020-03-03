from django.db import models

# Create your models here.
PLANT_CATEGORIES = (('Annuals', 'Annuals'), ('Biennials', 'Biennials'), ('Bulbs', 'Bulbs'), ('Cactus/Succulents', 'Cactus/Succulents'), ('Ferns', 'Ferns'), ('Groundcovers', 'Groundcovers'),
                        ('Herbs', 'Herbs'), ('Perennials', 'Perennials'), ('Shrubs', 'Shrubs'), ('Trees', 'Trees'), ('Vegetables', 'Vegetables'))

PLANT_HEIGHT = (('under 6in', 'under 6in'), ('6-12in', '6-12in'), ('1-3ft', '1-3ft'), ('4-10ft', '4-10ft'), ('12-20ft', '12-20ft'), ('over 20ft', 'over 20ft'))


class Plant(models.Model):
    name = models.CharField(max_length=35)
    family = models.CharField(max_length=25, blank=True)
    category = models.CharField(max_length=20, choices= PLANT_CATEGORIES)
    genus = models.CharField(max_length=25)
    primary_color = models.CharField(max_length=20)
    height = models.CharField(max_length=20, choices= PLANT_HEIGHT)
    year_sown = models.PositiveIntegerField(blank=True, null=True)

    Plants = models.Manager()

    def __str__(self):
        return self.name
