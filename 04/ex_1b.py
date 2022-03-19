from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_hard_rock_musicians_(N%E2%80%93Z)' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('a', {'title':re.compile('Q.*')})

links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

for link in links:
    print(link)

