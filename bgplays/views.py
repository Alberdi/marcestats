from django.shortcuts import get_object_or_404, render
from .models import Player

# Create your views here.
def player(request, player_name):
	player = get_object_or_404(Player, name=player_name)
	context = {'player': player}
	return render(request, 'bgplays/player.html', context)

