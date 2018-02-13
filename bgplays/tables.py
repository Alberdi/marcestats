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

    class Meta(SmallTable.Meta):
        model = Faction
        exclude = ('id', 'game',)
        prefix = 'faction'


class GameListTable(PagedTable):
    geek_id = tables.TemplateColumn(
        '{% if record.geek_id %}'
            '<a href="{{record.geek_url}}">{{record.geek_id}}</a>'
        '{% endif %}')
    last_played = tables.DateColumn(DATE_FORMAT)
    name = tables.LinkColumn('game', args=[A('id')])
    plays = tables.Column()

    class Meta(PagedTable.Meta):
        model = Game
        exclude = ('id',)


class GameTable(SmallTable):
    count = tables.Column()
    wins = tables.Column()
    name = tables.LinkColumn('game', args=[A('id')])

    class Meta(SmallTable.Meta):
        model = Game
        exclude = ('id',)
        prefix = 'game'


class PlayerListTable(PagedTable):
    birth_date = tables.DateColumn(DATE_FORMAT)
    name = tables.LinkColumn('player', args=[A('name')])
    last_played = tables.DateColumn(DATE_FORMAT)
    plays = tables.Column()

    class Meta(PagedTable.Meta):
        model = Player
        exclude = ('id',)


class PlayerTable(SmallTable):
    count = tables.Column()
    wins = tables.Column()
    name = tables.LinkColumn('player', args=[A('name')])

    class Meta(SmallTable.Meta):
        model = Player
        exclude = ('id', 'gender', 'birth_date',)
        prefix = 'player'


class PlayerMatesTable(SmallTable):
    count = tables.Column()
    name = tables.LinkColumn('player', args=[A('name')])

    class Meta(SmallTable.Meta):
        model = Player
        exclude = ('id', 'gender', 'birth_date',)
        prefix = 'mate'
