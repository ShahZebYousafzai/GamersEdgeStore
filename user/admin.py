from django.contrib import admin
from .models import Profile, ShippingAddress, UserPurchaseHistory, UserWishlist

# Register your models here.
admin.site.register(Profile)
admin.site.register(ShippingAddress)
admin.site.register(UserPurchaseHistory)
admin.site.register(UserWishlist)
