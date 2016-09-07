import django_tables2 as tables
from django_tables2.utils import A
from .models import *

DATE_FORMAT = "d/m/o"


class PagedTable(tables.Table):
    class Meta:
        template = 'bgplays/paged-table.html'
        per_page = 20


class SmallTable(tables.Table):
    class Meta:
        template = 'bgplays/small-table.html'
        per_page = 5


class FactionTable(SmallTable):
    count = tables.Column()
    wins = tables.Column()
    percentage = tables.Column()

    class Meta(SmallTable.Meta):
        model = Faction
        exclude = ('id', 'game',)
        prefix = 'faction'


class GameListTable(PagedTable):
    last_played = tables.DateColumn(DATE_FORMAT)
    name = tables.LinkColumn('game', args=[A('id')])
    plays = tables.Column()

    class Meta(PagedTable.Meta):
        model = Game
        exclude = ('id',)


class GameTable(SmallTable):
    count = tables.Column()
    name = tables.LinkColumn('game', args=[A('id')])

    class Meta(SmallTable.Meta):
        model = Game
        exclude = ('id',)
        prefix = 'game'


class PlayerListTable(PagedTable):
    birth_date = tables.DateColumn(DATE_FORMAT)
    name = tables.LinkColumn('player', args=[A('name')])

    class Meta(PagedTable.Meta):
        model = Player


class PlayerTable(SmallTable):
    count = tables.Column()
    name = tables.LinkColumn('player', args=[A('name')])
    wins = tables.Column()
    percentage = tables.Column()

    class Meta(SmallTable.Meta):
        model = Player
        exclude = ('id', 'gender', 'birth_date',)
        prefix = 'player'