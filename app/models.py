from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team/', null=True, blank=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Player(AbstractUser):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateTimeField('date of birth', null=True, blank=True)
    avatar = models.ImageField(upload_to='photos/', null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True)

    def __str__(self):
        return self.username


class Game(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='game/', null=True, blank=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    game = models.ForeignKey(Game)
    logo = models.ImageField(upload_to='tournament/', null=True, blank=True)
    description = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.game.name


class Match(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='match/', null=True, blank=True)
    description = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    first_team = models.ForeignKey(Team, related_name='first_team')
    second_team = models.ForeignKey(Team, related_name='second_team')
    tournament = models.ForeignKey(Tournament, null=True, blank=True)

    def __str__(self):
        return self.name

