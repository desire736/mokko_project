from django.contrib import admin
from .models import Publications, Coffees, Discord

# Register your models here.


@admin.register(Publications)
class PublicAdmin(admin.ModelAdmin):
   list_display = ['title']

@admin.register(Coffees)
class CoffeeAdmin(admin.ModelAdmin):
   list_display = ['name']

@admin.register(Discord)
class DiscordAdmin(admin.ModelAdmin):
   list_display = ['name']