from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Variant(models.Model):
    game = models.ForeignKey(Game)
    description = models.CharField(max_length=255)

    def __str__(self):
        return str((self.game, self.description))


class Faction(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str((self.game, self.name))


class Play(models.Model):
    game = models.ForeignKey(Game)
    minutes = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    variant = models.ForeignKey(Variant, null=True, blank=True)
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
    play = models.ForeignKey(Play)
    players = models.ManyToManyField(Player)
    factions = models.ManyToManyField(Faction, blank=True)
    points = models.IntegerField(null=True, blank=True)
    winner = models.NullBooleanField(null=True)

    def __str__(self):
        return str((self.play, self.points, self.winner))
