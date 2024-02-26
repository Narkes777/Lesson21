from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

class Match(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True, related_name='player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    result = models.BooleanField(null=True, blank=True)
    data = models.DateTimeField()