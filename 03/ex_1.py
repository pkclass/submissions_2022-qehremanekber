from urllib import request
from bs4 import BeautifulSoup as BS

# Download and import to Beautiful Soup already known page:
url = 'http://www.pythonscraping.com/pages/warandpeace.html' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

selected_tags = bs.find_all(lambda tag: (tag.get_text()) == "Anna Pavlovna")

def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

print("Number of tags", get_number_of_elements(selected_tags))

selected_tags2 = bs.find_all(lambda tag: (len(tag.attrs) == 1))
for tag in selected_tags2:
    print('*****************')
    print(tag.get_text())

print("lenght", get_number_of_elements(selected_tags2))

