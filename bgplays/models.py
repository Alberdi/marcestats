from django.db import models


class Game(models.Model):
    BOARD_GAME = 'B'
    RPG = 'R'
    TYPE_CHOICES = ((BOARD_GAME, 'Board game'), (RPG, 'Role-playing game'))
    geek_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES,
                            default=BOARD_GAME)

    def geek_url(self):
        if not self.geek_id:
            return None
        if self.type == self.RPG:
            return "https://rpggeek.com/rpgitem/" + str(self.geek_id)
        else:
            return "https://boardgamegeek.com/boardgame/" + str(self.geek_id)


    def __str__(self):
        return self.name


class Variant(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255)

    def __str__(self):
        return str((self.game, self.description))


class Faction(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str((self.game, self.name))


class Play(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    minutes = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    virtual = models.BooleanField(default=False)
    variant = models.ForeignKey(Variant, null=True, blank=True,
                                on_delete=models.DO_NOTHING)
    comments = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return str((self.id, self.game, self.date))


class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'))
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    play = models.ForeignKey(Play, on_delete=models.DO_NOTHING)
    players = models.ManyToManyField(Player)
    factions = models.ManyToManyField(Faction, blank=True)
    points = models.IntegerField(null=True, blank=True)
    winner = models.NullBooleanField(null=True)

    def __str__(self):
        return str((self.play, self.points, self.winner))
