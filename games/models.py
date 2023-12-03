import uuid
from django.db import models
from django.contrib.auth.models import User


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

class GameOrder(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_bought = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        gameitems = self.gameitem_set.all()
        total = sum([gameitem.get_total for gameitem in gameitems])
        return total

    @property
    def get_cart_items(self):
        gameitems = self.gameitem_set.all()
        total = sum([gameitem.quantity for gameitem in gameitems])
        return total

class GameItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(GameOrder, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.game.title

    @property
    def get_total(self):
        total = self.product_price
        return total
    
    @property
    def quantity(self):
        return 1