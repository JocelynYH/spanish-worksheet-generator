# import bs4 as
from bs4 import BeautifulSoup as bs
import urllib.request
import requests


def getSentences(word):
    page = requests.get(
        'https://www.spanishdict.com/translate/{}'.format(word))

    soup = bs(page.content, 'html.parser')

    dictionaryContainer = soup.find(id="dictionary-neodict-es")

    listEnglishSentences = [sentence.get_text()
                            for sentence in list(dictionaryContainer.find_all('em'))]
    listSpanishSentences = [sentence.previous_sibling.previous_sibling.get_text()
                            for sentence in list(dictionaryContainer.find_all('em'))]

    exampleSentencesDictionary = []

    for sentence, sentenceES in zip(listEnglishSentences, listSpanishSentences):
        exampleSentencesDictionary.append({
            'english': sentence,
            'spanish': sentenceES
        })

    return exampleSentencesDictionary


# result = getSentences("pillar")

# print(result)
