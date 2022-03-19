from urllib import request
from bs4 import BeautifulSoup as BS
import re

# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians#R' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('a', {'title':re.compile('List of [Rr].*')})

links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

for link in links:
    print(link)