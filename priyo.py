import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

questionlist = []

def getQuestions(tag):
    url = f'https://bangla.bdnews24.com/{tag}?tab=Active'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'custombody print-only'})
    for item in questions:
        question = {
        'tag': tag,  
        #'title': item.find('div', {'class': 'pl-2 pr-2 article-heading pt-2'}).text,
        #'link': 'https://www.priyo.com' + item.find('a', {'class': 'content-feed-anchor priyo-hover'})['href'],
        'summary': item.find('p').text,
        #'commentator': 'https://www.priyo.com' +  item.find('a', {'class': ' UFICommentActorName'})['href'],
        #'comments': str(item.find('span', {'class': '_5mdd'}).text),


        }
        questionlist.append(question)
    return

for x in range(1):
    getQuestions('samagrabangladesh/article1835879.bdnews')


df = pd.DataFrame(questionlist)
df.to_csv('fullArticle.csv', index=False)
print('Fin.')
