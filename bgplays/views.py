from django.shortcuts import get_object_or_404, render
from .models import Player
import services

# Create your views here.
def player(request, player_name):
	p = get_object_or_404(Player, name=player_name)
	most_played_games = services.get_most_played_games(p.id)
	most_played_mates = services.get_most_played_mates(p.id)
	context = {'player': p,
               'most_played_games': most_played_games,
               'most_played_mates': most_played_mates}
	return render(request, 'bgplays/player.html', context)

