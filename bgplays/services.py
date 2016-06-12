from models import *

# Player info services
def get_most_played_games(player_id, count=5):
    plays_ids = get_play_ids(player_id)
    return Play.objects.filter(id__in=plays_ids) \
               .annotate(name=F('game__name')) \
               .values('name') \
               .annotate(count=Count('name')) \
               .order_by('-count')[:count]

def get_most_played_mates(player_id, count=5):
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
