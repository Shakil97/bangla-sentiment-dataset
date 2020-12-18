import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

questionlist = []

def getQuestions(tag):
    url = f'https://www.priyo.com/{tag}?tab=Active'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'mb-2 feed feed-horizontal'})
    for item in questions:
        question = {
        'tag': tag,  
        'title': item.find('a', {'class': 'content-feed-anchor priyo-hover'}).text,
        'link': 'https://www.priyo.com' + item.find('a', {'class': 'content-feed-anchor priyo-hover'})['href'],
        #'publisher': item.find('span', {'class': 'f-16 pt-1'}).text,
        #'date': item.find('span', {'class': 'pub-date'}).date,
        }
        questionlist.append(question)
    return

for x in range(1):
    getQuestions('sports')
    getQuestions('politics')
    getQuestions('bangladesh')
    getQuestions('science')
    getQuestions('international')


df = pd.DataFrame(questionlist)
df.to_csv('priyo.csv', index=False)
print('Fin.')
