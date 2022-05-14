from urllib import request
from urllib.request import Request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd
import os

url = 'https://myanimelist.net/anime.php#'
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = request.urlopen(request_site)
bs = BS(html.read(), 'html.parser')
tags = bs.find_all('a', {'class':'genre-name-link'})[:18]

links = [ 'https://myanimelist.net' + tag['href'] for tag in tags]

################################################ movies #######################################################################
webpages = []

for link in links:
    
    print(link)
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')

    tags = bs.find_all('a', {'class':'link-image'})[:40]
    try: 
        links = [tag['href'] for tag in tags]
    except:
        pass
    webpages.extend(links)



##################################### movie details ###########################################################################

d = pd.DataFrame({'name':[], 'score':[], 'rank':[], 'popularity':[], 'members':[], 'date':[], 'date':[], 'channel':[]})

for link in webpages:
    try:
        print(link)
        html = request.urlopen(link)
        bs = BS(html.read(), 'html.parser')

        try:
            name = bs.find('strong').text
        except:
            name = 'NA'
        
        try:
            scoreboard = bs.find('div', {'class':'fl-l score'})
            score = scoreboard.find('div').text
        except:
            score = 'NA'
        
        try:
            tomatometer = bs.find('span', {'class':'rottentomatoes-icon rottentomatoes-icon--flat icon-rottom-flat-rotten'}).findNext('span').text
        except:
            tomatometer = 'NA'

        try:
            tank = bs.find('span', {'class':'numbers ranked'})
            rank = tank.find('strong').text
        except:
            rank = 'NA'
        
        try:
            topu = bs.find('span', {'class':'numbers popularity'})
            popu = topu.find('strong').text
        except:
            popu = 'NA'
        
        try:
            tember = bs.find('span', {'class':'numbers members'})
            member = tember.find('strong').text
        except:
            member = 'NA'

        try:
            tate = bs.find('span', {'class':'information season'})
            date = tate.find('a').text
        except:
            date = 'NA'
        
        try:
            cchannel = bs.find('span', {'class':'information type'})
            channel = cchannel.find('a').text
        except:
            channel = 'NA'

        movies = {'name':name, 'score':score, 'rank':rank , 'popularity':popu, 'members':member, 'date':date, 'channel':channel }

        d = d.append(movies, ignore_index = True)
        print(d)
    except: 
        d

d.to_csv('animes2.csv')
