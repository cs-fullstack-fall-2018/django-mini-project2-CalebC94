from django.db import models


class MusicPlaylist(models.Model):
    songName = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    duration = models.FloatField()
    rating = models.IntegerField()


def __str__(self):
    return self.name