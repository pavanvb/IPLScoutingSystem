from django.shortcuts import render
from django.http import HttpResponse
from .models.player import Player

# Create your views here.
def index(request):
   players=Player.get_all_players();
   print(players)
   return render(request,'IPLAPP/index.html',{'players': players})
    #return render(request, 'home.html')


