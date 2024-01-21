from django.db import models
from games.models import Game, Genre
from games.models import GameOrder, GameItem
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    date_of_birth = models.DateField(null=True, blank=True)
    wishlist = models.ForeignKey('UserWishlist', on_delete=models.CASCADE, null=True, blank=True)
    purchase_history = models.ForeignKey('UserPurchaseHistory', on_delete=models.CASCADE, null=True, blank=True)
    genre_preferences = models.ManyToManyField(Genre)  # Many-to-many relationship with genres
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    # order = models.ForeignKey(GameOrder, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class UserPurchaseHistory(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_profile.user.username

class UserWishlist(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_profile.user.username