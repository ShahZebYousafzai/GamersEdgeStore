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
    digital = models.BooleanField(default=False, null=True, blank=True)
    Description = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre)
    # digital = models.BooleanField(default=True, null=True, blank=False) # For physical item

    def __str__(self):
        return self.title

class GameOrder(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_bought = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    # For physical item
    @property
    def shipping(self):
        shipping = False
        gameitems = self.gameitem_set.all()
        for i in gameitems:
            if i.game.digital==False:
                # print("Item will need to be shipped")
                shipping=True
            # print("Item will not need to be shipped")
        return shipping

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
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(GameOrder, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.game.title

    @property
    def get_total(self):
        price = self.game.price
        return price
    
    @property
    def quantity(self):
        return 1