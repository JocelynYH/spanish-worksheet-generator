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
# print(soup.prettify())
list(soup.children)