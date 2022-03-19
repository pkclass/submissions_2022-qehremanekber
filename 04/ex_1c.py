#From the page linked above extract extract: the name of the band, the
#genre, number of years active.

from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

d = pd.DataFrame({'name':[], 'genre':[], 'years':[], })

url = 'https://en.wikipedia.org/wiki/Queen_(band)' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

try:
    name = bs.find('h1').text
except:
    name = ''

try:
    genre = bs.find('th',string = 'Genres').next_sibling.text
except:
    genre = ''

try:
    years = bs.find('th',string = 'Years active').next_sibling.text
except:
    years = ''

painter = {'name':name, 'genre':genre, 'years':years,}

d = d.append(painter, ignore_index = True)

print(d)
