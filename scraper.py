# import bs4 as
from bs4 import BeautifulSoup as bs
import urllib.request
import requests

word = "pillar"
# source = urllib.request.urlopen('https://www.spanishdict.com/translate/pillar')

page = requests.get('https://www.spanishdict.com/translate/pillar')
# source = urllib.request.urlopen('https://www.spanishdict.com/translate/%s) % word


# soup = bs.BeautifulSoup(page, 'lxml')

soup = bs(page.content, 'html.parser')
# print(soup.children[0])

# print(list(soup.children))

# print([type(item) for item in list(soup.children)])

# html = list(soup.children)[1]

# print(list(html.children)[1])

# print(soup.find_all(id='dictionary-neodict-es').children[0])
# print(soup.find_all('em'))

enToSp = soup.find(id='translate-en')
# print(enToSp[0, 10])
# print([type(item) for item in list(enToSp.children)])
# print(list(enToSp.children))
#
# print(enToSp)

# print([for item in list(enToSp.find_all('em').get_text())

# for eng in enToSp.find_all('em'):
# print(eng.get_text())

listEmTags = enToSp.find_all('em')
print([item.get_text() for item in list(listEmTags)])

# print(enToSp).find_all('em')
print(enToSp.find_all('em')[0])
