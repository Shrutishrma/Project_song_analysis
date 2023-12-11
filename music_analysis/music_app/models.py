# music_analysis/models.py
from django.db import models

class Song(models.Model):
    track_name = models.CharField(max_length=255, default='')
    album_name = models.CharField(max_length=255, default='')
    artist_names = models.CharField(max_length=255, default='')
    release_year = models.IntegerField(default=0)
    duration_in_min = models.FloatField(default=0.0)
    popularity = models.FloatField(default=0.0)
    genres = models.TextField(default='')
    danceability = models.FloatField(default=0.0)
    energy = models.FloatField(default=0.0)
    key = models.IntegerField(default=0)
    loudness = models.FloatField(default=0.0)
    mode = models.IntegerField(default=0)
    speechiness = models.FloatField(default=0.0)
    acousticness = models.FloatField(default=0.0)
    instrumentalness = models.FloatField(default=0.0)
    liveness = models.FloatField(default=0.0)
    valence = models.FloatField(default=0.0)
    tempo = models.FloatField(default=0.0)
    time_signature = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.track_name} by {self.artist_names}"