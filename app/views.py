from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# Create your views here.
def get_stats(player):
    url = "http://www.nfl.com/player/profile{}".format(player)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    current_player = souper.find(class_="stats")
    player_url = current_player.a.attrs["href"]
    content = requests.get(player_url).text
    return current_player


def player_scraping_view(request):
    player = request.GET.get('player') or "Brett Farve"
    current_player = get_stats(player)
    #player_id = urlparse(current_player.attrs("href")).query.strip("id")
    #content = requests.get('http://www.nfl.com/player/drewbrees/2504775/profile')
    #souper = BeautifulSoup(content.text, "html.parser")
    return render(request,"index.html", {"current_player": current_player,"player": player})
