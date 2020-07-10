from django.db import models


class Player(models.Model):
    search_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Game(models.Model):
    is_finished = models.BooleanField(default=False)
    creator = models.IntegerField(blank=True, null=True)
    right_answer = models.IntegerField(blank=True, null=True)
    players = models.ManyToManyField('Player', through='PlayerGameInfo', related_name='games')

    def __str__(self):
        return str(self.id)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    try_counts = models.IntegerField(default=0)