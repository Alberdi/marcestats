from django.contrib import admin

from .models import Faction
from .models import Game
from .models import Play
from .models import Player
from .models import Team
from .models import Variant

admin.site.register(Faction)
admin.site.register(Game)
admin.site.register(Play)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Variant)

