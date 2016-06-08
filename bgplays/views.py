from django.shortcuts import get_object_or_404, render
from .models import Player
import services

# Create your views here.
def player(request, player_name):
	player = get_object_or_404(Player, name=player_name)
	most_played_games = services.get_most_played_games(player.id)
	context = {'player': player, 'most_played_games': most_played_games}
	return render(request, 'bgplays/player.html', context)

