from django.db import models
class Scouting(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
