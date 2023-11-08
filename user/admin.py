from django.contrib import admin
from .models import UserProfile, PurchaseHistory

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(PurchaseHistory)
