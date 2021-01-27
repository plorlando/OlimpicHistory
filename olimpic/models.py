from django.db import models


class Noc(models.Model):
    noc = models.CharField(max_length=3, primary_key=True)
    region = models.CharField(max_length=100)
    notes = models.CharField(max_length=100, blank=True, null=True)


class Athlete_events(models.Model):
    id_athlete = models.IntegerField()
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    age = models.PositiveIntegerField()
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    team = models.CharField(max_length=50)
    noc = models.ForeignKey(Noc, max_length=3, verbose_name='NOC', on_delete=models.CASCADE)
    games = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    season = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    sport = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    medal = models.CharField(max_length=10)




