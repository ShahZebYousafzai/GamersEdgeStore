from django.db import models
from games.models import Game, Genre
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(default='profiles/default.png', upload_to='profiles/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    # game_library = models.ManyToManyField(Game)
    # wishlist = models.ManyToManyField(Game)
    purchase_history = models.ForeignKey('PurchaseHistory', on_delete=models.CASCADE, null=True, blank=True)
    genre_preferences = models.ManyToManyField(Genre)  # Many-to-many relationship with genres

    def __str__(self):
        return str(self.user)


class PurchaseHistory(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_profile
