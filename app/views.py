from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup



# Create your views here.
def player_scraping_view(request):
    player = request.GET.get('player') or "Joe Flacco"
    url = "http://www.nfl.com/search?query={}".format(player)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    data_table = souper.find(class_="stats").attrs["href"]
    content = requests.get(data_table).text
    souper = BeautifulSoup(content, "html.parser")
    player_stats = str(souper.find(id="main-content"))
    return render(request,"index.html",{"data_table": data_table, "player_stats": player_stats})

#def player_scraping_view(request):
    #player = request.GET.get('player') or "Drew Brees"
    #current_player = get_stats(player)
    #player_id = urlparse(current_player.attrs("href")).query.strip("id")
    #content = requests.get('http://www.nfl.com/player/drewbrees/2504775/profile')
    #souper = BeautifulSoup(content.text, "html.parser")
    #return render(request,"index.html",{"current_player": current_player,"player": player})
