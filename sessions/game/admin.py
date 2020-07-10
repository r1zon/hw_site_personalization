from django.contrib import admin

from game.models import Player, Game, PlayerGameInfo

# class PlayerGameInfoInline(admin.TabularInline):
#     model=PlayerGameInfo

class PlayerAdmin(admin.ModelAdmin):
    pass

class GameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
# admin.site.register(PlayerGameInfo, PlayerGameInfoInline)