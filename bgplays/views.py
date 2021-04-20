from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django_tables2 import RequestConfig
from .models import *
from .services import *
from .tables import *


def game_list(r):
    games = tablify(get_game_list(),
                    GameListTable, r)
    context = {'games': games}
    return render(r, 'bgplays/game_list.html', context)


def game(r, game_id):
    g = get_game_list().filter(id=game_id).first()
    if not g: raise Http404('Game not found')
    faction_plays = tablify(get_faction_plays(g.id),
                            FactionTable, r, 'Factions')
    game_players = tablify(get_game_players(g.id),
                           PlayerTable, r, 'Players')
    context = {'game': g,
               'median_points': get_median_points(g.id),
               'faction_plays': faction_plays,
               'game_players': game_players}
    return render(r, 'bgplays/game.html', context)


def player_list(r):
    players = tablify(get_player_list(),
                      PlayerListTable, r)
    context = {'players': players}
    return render(r, 'bgplays/player_list.html', context)


def player(r, player_name):
    p = get_player_list().filter(name=player_name).first()
    if not p: raise Http404('Player not found')
    player_games = tablify(get_player_games(p.id),
                           GameTable, r, 'Played games')
    player_mates = tablify(get_player_mates(p.id),
                           PlayerMatesTable, r, 'Mates')
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
