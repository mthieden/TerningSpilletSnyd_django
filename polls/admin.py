from django.contrib import admin

from .models import  User, Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('port', 'user', 'dice', 'players')

admin.site.register(User)


admin.site.register(Game, GameAdmin)
