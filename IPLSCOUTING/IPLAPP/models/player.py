from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    team = models.CharField(max_length=50)
    baseprice = models.CharField(max_length=50 )
    shortlisted = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/players/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_players():
        return Player.objects.all()
