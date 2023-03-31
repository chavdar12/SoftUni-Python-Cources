from django.db import models

from django_102.models.player import Player


class GameManager(models.Manager):
    def all_with_players_count(self):
        return self.all()\
                .annotate(players_count=models.Count('players'))


class Game(models.Model):
    objects = GameManager()

    DIFFICULTY_LEVEL_CHOICES = (
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard')
    )
    name = models.CharField(max_length=30, blank=False)
    difficulty_level = models.CharField(max_length=6, blank=False, choices=DIFFICULTY_LEVEL_CHOICES)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return f'{self.name}'
