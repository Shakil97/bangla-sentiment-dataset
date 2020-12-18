#import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

questionlist = []

def getQuestions(tag,page):
    url = f'https://sarabangla.net/{tag}?tab=Active&page={page}&pagesize=50'
    session = HTMLSession()
    r = session.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'blunt-post'})
    for item in questions:
        question = {
        'tag': tag,  
        'title': item.find('h2', {'class': 'post-title'}).text,
        #'link': 'https://www.bbc.com/bengali' + item.find('a', {'class': 'css-wla3o-Link evnt13t2'})['href'],
        'summary': item.find('p').text,
        #'description':item.find('p', {'class': 'css-qwzmjb-Paragraph e1cc2ql70'}).text,
               
        }
        questionlist.append(question)
    return

for x in range(1,40):
    getQuestions('entertainment/world',x)
    
    

df = pd.DataFrame(questionlist)
df.to_csv('sarabangla.csv', index=False)
print('Fin.')
