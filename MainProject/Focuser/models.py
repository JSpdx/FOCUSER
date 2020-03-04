from django.db import models

ECLIPSE_TYPE = (('Solar', 'Solar'), ('Lunar', 'Lunar'))
ECLIPSE_SUBTYPE = (('Penumbral', 'Penumbral'), ('Annular', 'Annular'), ('Total', 'Total',), ('Partial', 'Partial'))

class Eclipse(models.Model):
    date = models.CharField(max_length=20, blank=False, null=True)
    locations = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=20, choices= ECLIPSE_TYPE)
    subtype = models.CharField(max_length=50, choices = ECLIPSE_SUBTYPE)
    description = models.CharField(max_length=1000, blank= True, null = True)

    Eclipses = models.Manager()

    def __str__(self):
        return self.date