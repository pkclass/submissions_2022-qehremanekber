from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

url = 'https://www.pythonscraping.com/pages/page3.html' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

#extract bolded parts
bs_name_list = bs.find_all('span', {'class':'excitingNote'})

name_list = [name.get_text() for name in bs_name_list]

# The data can be put into data frame, later into .csv file.
d = pd.DataFrame(name_list)
print(d)

#footer
print("footer")
footer = bs.find('div', {'id':'footer'}).text
print(footer)

print("last item title")

#Extract the last Item Title from the table.
last = bs.find('tr', {'id':'gift5'}).td.text
print(last)