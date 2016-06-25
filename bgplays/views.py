from django.shortcuts import get_object_or_404, render
from django_tables2 import RequestConfig
from .models import *
import tables
import services


def game(r, game_id):
    g = get_object_or_404(Game, id=game_id)
    faction_plays = tablify(services.get_faction_plays(g.id),
                            tables.FactionTable, r, 'Factions')
    game_players = tablify(services.get_game_players(g.id),
                           tables.PlayerTable, r, 'Players')
    context = {'game': g,
               'median_points': services.get_median_points(g.id),
               'play_count': services.get_play_count(g.id),
               'faction_plays': faction_plays,
               'game_players': game_players}
    return render(r, 'bgplays/game.html', context)


def player(r, player_name):
    p = get_object_or_404(Player, name=player_name)
    player_games = tablify(services.get_player_games(p.id),
                           tables.GameTable, r, 'Played games')
    player_mates = tablify(services.get_player_mates(p.id),
                           tables.PlayerTable, r, 'Mates')
    context = {'player': p,
               'player_games': player_games,
               'player_mates': player_mates}
    return render(r, 'bgplays/player.html', context)


# Helper methods
def tablify(data, TableClass, request, title=None):
    table = TableClass(data)
    table.title = title
    RequestConfig(request).configure(table)
    return table