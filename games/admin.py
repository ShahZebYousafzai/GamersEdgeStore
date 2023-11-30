from django.contrib import admin
from .models import Game, Genre, GameOrder, GameItem

# Register your models here.
admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(GameOrder)
admin.site.register(GameItem)
# admin.site.register(Platform)
# admin.site.register(Publisher)