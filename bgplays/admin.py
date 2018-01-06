from django.contrib import admin

from .models import Faction
from .models import Game
from .models import Play
from .models import Player
from .models import Team
from .models import Variant

class TeamInline(admin.StackedInline):
	model = Team
	extra = 2
	filter_horizontal = ('players', 'factions',)

class PlayAdmin(admin.ModelAdmin):
	inlines = [TeamInline]
	save_as = True

admin.site.register(Faction)
admin.site.register(Game)
admin.site.register(Play, PlayAdmin)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Variant)

