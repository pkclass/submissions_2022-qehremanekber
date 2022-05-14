from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Lists_of_musicians'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('a', {'title':re.compile('List of [Aa].*')})

links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

################################################################################
# This part prepares real painter links
################################################################################

webpages = []

for link in links:
    print(link)
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')
    
    tags = bs.find_all('ul')[1].find_all('li')

    link_temp_list = []
    for tag in tags:
        try:
            link_temp_list.append('http://en.wikipedia.org' + tag.a['href'])
        except:
            0 

    webpages.extend(link_temp_list)

################################################################################
# This part scraps painters
################################################################################
d = pd.DataFrame({'name':[], 'years':[]})

for webpage in webpages[:100]:
    print(webpage)

    html = request.urlopen(webpage)
    bs = BS(html.read(), 'html.parser')
    
    try:
        name = bs.find('h1').text
    except:
        name = ''
    
    try:
        years = bs.find('th',string = 'Years active').next_sibling.text
    except:
        years = ''

    painter = {'name':name, 'years':years}
    
    d = d.append(painter, ignore_index = True)
    print(d)

d.to_csv('musicians.csv')
