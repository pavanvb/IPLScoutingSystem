from django.contrib import admin
from .models.player import Player
from .models.HigherAuthority import Higher_authority
from .models.Scouting import Scouting


class Adminplayer(admin.ModelAdmin):
    list_display = ['id','name','age','team','baseprice','shortlisted','country','state']

class AdminHigherauthority(admin.ModelAdmin):
    list_display = ['name','age']

class AdminScouting(admin.ModelAdmin):
    list_display = ['name','age']


# Register your models here.
admin.site.register(Player,Adminplayer)
admin.site.register(Higher_authority,AdminHigherauthority)
admin.site.register(Scouting,AdminScouting)
