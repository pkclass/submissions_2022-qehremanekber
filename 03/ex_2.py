

from urllib import request
from bs4 import BeautifulSoup as BS
import re


# Download and import to Beautiful Soup already known page:
url = 'https://en.wikipedia.org/wiki/United_Nations_Development_Programme' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

imglinks = bs.find_all('a', attrs = {'class':'image'})[0]
for img in imglinks.find_all('img'):
    print(img['src'].replace('//','https://'))
