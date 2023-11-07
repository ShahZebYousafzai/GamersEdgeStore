import uuid
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    image_cover_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=100)
    Description = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title