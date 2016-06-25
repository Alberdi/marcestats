import django_tables2 as tables
from django_tables2.utils import A
from .models import *


class SmallTable(tables.Table):
    class Meta:
        template = 'bgplays/small-table.html'
        per_page = 5


class FactionTable(SmallTable):
    count = tables.Column()
    wins = tables.Column()

    class Meta(SmallTable.Meta):
        model = Faction
        exclude = ('id', 'game',)
        prefix = 'faction'


class GameTable(SmallTable):
    count = tables.Column()
    name = tables.LinkColumn('game', args=[A('id')])

    class Meta(SmallTable.Meta):
        model = Game
        exclude = ('id',)
        prefix = 'game'


class PlayerTable(SmallTable):
    count = tables.Column()
    name = tables.LinkColumn('player', args=[A('name')])

    class Meta(SmallTable.Meta):
        model = Player
        exclude = ('id', 'gender', 'birth_date',)
        prefix = 'player'
