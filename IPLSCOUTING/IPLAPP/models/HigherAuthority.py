from django.db import models

class Higher_authority(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
