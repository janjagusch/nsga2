import os
import urllib.request
import requests
import bs4 as bs
import pandas as pd


def _get_player_url(player_id):
    return "https://www.futbin.com/19/player/{}".format(player_id)


def _get_player_img_url(player_id):
    url = _get_player_url(player_id)
    r = requests.get(url)
    s = bs.BeautifulSoup(r.content, "html.parser")
    img_url = s.find("img", {"id": "player_pic", "class": "pcdisplay-picture-width"})["src"]
    return img_url


def _get_player_img(player_id):
    url = _get_player_img_url(player_id)
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    img = response.read()
    return img


def scrape_player_img(player_id, filepath="../input/pictures/"):
#     stored_players = pd.Series(os.listdir(filepath)).str.replace(".png", "")
#     if player_id not in stored_players:
    filename = "{}.png".format(player_id)
    img = _get_player_img(player_id)
    with open(os.path.join(filepath, filename), "wb") as f:
        f.write(img)
