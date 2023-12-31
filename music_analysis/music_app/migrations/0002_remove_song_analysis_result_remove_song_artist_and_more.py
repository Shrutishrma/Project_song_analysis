# Generated by Django 4.2.5 on 2023-12-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='analysis_result',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='song',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='song',
            name='title',
        ),
        migrations.AddField(
            model_name='song',
            name='acousticness',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='song',
            name='album_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='song',
            name='artist_names',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='song',
            name='danceability',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='song',
            name='duration_in_min',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='song',
            name='energy',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='song',
            name='genres',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='song',
            name='instrumentalness',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='song',
            name='key',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='liveness',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='song',
            name='loudness',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='song',
            name='mode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='popularity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='release_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='speechiness',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='song',
            name='tempo',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='song',
            name='time_signature',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='track_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='song',
            name='valence',
            field=models.FloatField(default=0.0),
        ),
    ]
