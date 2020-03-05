from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=100, null=True)
    artist = models.CharField(max_length=100)

    Albums = models.Manager()

    def __str__(self):
        return self.title