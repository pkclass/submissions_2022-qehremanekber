from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')
bs.encode("utf-8")

print("birthdate")
birth = bs.find('span', {'class':'bday'}).text
print(birth)

print("occupations")
occup = bs.find_all('td', {'class':'infobox-data role'})
for name in occup:
    print(name.get_text())
name_list = [name.get_text() for name in occup]



print("references")
bs_refer_list = bs.find_all('span', {'class':'reference-text'})
for name in bs_refer_list:
    print(name.get_text())
