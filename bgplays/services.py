from models import *
from django.db.models import Count, fields, F, Sum
from django.db.models.expressions import ExpressionWrapper


# Game info services
def get_median_points(game_id):
    return median_value(Team.objects.filter(play__game__id=game_id) \
                        .exclude(play__team__points__isnull=True),
                        'play__team__points')


def get_play_count(game_id):
    return Play.objects.filter(game__id=game_id).count()


def get_game_players(game_id):
    play_players = Play.objects.filter(game__id=game_id) \
        .annotate(name=F('team__players__name')) \
        .annotate(winner=F('team__winner')) \
        .annotate(pid=F('team__players__id')) \
        .values('id', 'name', 'pid', 'winner').distinct()
    return Player.objects.raw(
        '''SELECT pid, name, COUNT(DISTINCT id) AS 'count', SUM(winner) AS 'wins',
           100*SUM(winner)/COUNT(DISTINCT id) AS 'percentage'
           FROM ( %s )
           GROUP BY pid ORDER BY COUNT(id) DESC, SUM(winner) DESC''' % str(play_players.query),
        translations={'pid': 'id'})


def get_faction_plays(game_id):
    return Faction.objects.filter(game__id=game_id) \
        .values('name') \
        .annotate(wins=Sum('team__winner')) \
        .annotate(count=Count('name')) \
        .annotate(percentage=ExpressionWrapper(100 * F('wins') / F('count'), output_field=fields.IntegerField())) \
        .order_by('-count', '-wins')


# Player info services
def get_player_games(player_id):
    plays_ids = get_play_ids(player_id)
    return Game.objects.filter(play__id__in=plays_ids) \
        .values('name', 'id') \
        .annotate(count=Count('name')) \
        .order_by('-count')


def get_player_mates(player_id):
    # XXX: That distinct() is probably not working as expected
    # But there are not counterexamples in the current data set
    plays_ids = get_play_ids(player_id)
    return Player.objects.filter(team__play__id__in=plays_ids) \
        .exclude(id=player_id) \
        .values('name', 'team__play__id') \
        .distinct() \
        .values('name') \
        .annotate(count=Count('name')) \
        .annotate(wins=Sum('team__winner')) \
        .annotate(percentage=ExpressionWrapper(100 * F('wins') / F('count'), output_field=fields.IntegerField())) \
        .order_by('-count')


# Helper methods
def get_play_ids(player_id):
    return Play.objects.filter(team__players__id=player_id).values('id').distinct()


def median_value(queryset, term):
    count = queryset.count()
    values = queryset.values_list(term, flat=True).order_by(term)
    if count % 2 == 1:
        return values[int(round(count / 2))]
    elif count > 0:
        return sum(values[count / 2 - 1:count / 2 + 1]) / 2.0
    else:
        return 0
