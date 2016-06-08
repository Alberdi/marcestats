from models import *

def get_most_played_games(player_id, count=5):
	plays_ids = Team.objects.filter(players__id=player_id).values('play__id')
	return Play.objects.filter(id__in=plays_ids)\
			.annotate(name=F('game__name'))\
			.values('name')\
			.annotate(count=Count('name'))\
			.order_by('-count')[:count]

