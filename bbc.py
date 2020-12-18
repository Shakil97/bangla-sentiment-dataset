import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

questionlist = []

def getQuestions(tag):
    url = f'https://www.bbc.com/{tag}?tab=Active'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'css-8tq3w8 ezetrkd0'})
    for item in questions:
        question = {
        'tag': tag,  
        'title': item.find('a', {'class': 'css-wla3o-Link evnt13t2'}).text,
        'link': 'https://www.bbc.com/bengali' + item.find('a', {'class': 'css-wla3o-Link evnt13t2'})['href'],
        'summary': item.find('p', {'class': 'css-193xxgh-Summary e1tfxkuo4'}).text,
        'date': item.find('time', {'class': 'css-lt7vf0-StyledTimestamp e4zesg50'}).text,
        }
        questionlist.append(question)
    return

for x in range(1):
    getQuestions('bengali')
    #getQuestions('flask', x)

df = pd.DataFrame(questionlist)
df.to_csv('bbc.csv', index=False)
print('Fin.')
