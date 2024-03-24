from django.contrib import admin

# Register your models here.
from django_102.models.game import Game
from django_102.models.player import Player

admin.site.register(Game)
admin.site.register(Player)