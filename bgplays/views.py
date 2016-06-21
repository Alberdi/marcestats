from django.shortcuts import get_object_or_404, render
from .models import Game, Player
import services


def game(request, game_id):
    g = get_object_or_404(Game, id=game_id)
    context = {'game': g,
               'play_count': services.get_play_count(g.id),
               'most_played_players': services.get_most_played_players(g.id)}
    return render(request, 'bgplays/game.html', context)


def player(request, player_name):
    p = get_object_or_404(Player, name=player_name)
    most_played_games = services.get_most_played_games(p.id)
    most_played_mates = services.get_most_played_mates(p.id)
    context = {'player': p,
               'most_played_games': most_played_games,
               'most_played_mates': most_played_mates}
    return render(request, 'bgplays/player.html', context)
