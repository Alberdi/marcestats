from models import *
from django.db.models import Avg, Count, F, Sum


# Game info services
def get_avg_points(game_id):
    return Team.objects.filter(play__game__id=game_id) \
        .exclude(play__team__points__isnull=True) \
        .aggregate(avg=Avg('play__team__points'))['avg']


def get_play_count(game_id):
    return Play.objects.filter(game__id=game_id).count()


def get_most_played_players(game_id, count=5):
    play_players = Play.objects.filter(game__id=game_id) \
        .annotate(name=F('team__players__name')) \
        .annotate(pid=F('team__players__id')) \
        .values('id', 'name', 'pid').distinct()
    return Player.objects.raw(
        '''SELECT pid, name, COUNT(*) AS 'count' FROM ( %s )
           GROUP BY pid ORDER BY COUNT(pid) DESC''' % str(play_players.query),
        translations={'pid': 'id'})[:count]


def get_most_faction_plays(game_id, count=5):
    return Faction.objects.filter(game__id=game_id) \
               .values('description') \
               .annotate(wins=Sum('team__winner')) \
               .annotate(count=Count('description')) \
               .order_by('-count', '-wins')[:count]


# Player info services
def get_most_played_games(player_id, count=5):
    plays_ids = get_play_ids(player_id)
    return Game.objects.filter(play__id__in=plays_ids) \
               .values('name', 'id') \
               .annotate(count=Count('name')) \
               .order_by('-count')[:count]


def get_most_played_mates(player_id, count=5):
    # XXX: That distinct() is probably not working as expected
    # But there are not counterexamples in the current data set
    plays_ids = get_play_ids(player_id)
    return Player.objects.filter(team__play__id__in=plays_ids) \
               .exclude(id=player_id) \
               .values('name', 'team__play__id') \
               .distinct() \
               .values('name') \
               .annotate(count=Count('name')) \
               .order_by('-count')[:count]


# Helper methods
def get_play_ids(player_id):
    return Play.objects.filter(team__players__id=player_id).values('id').distinct()
