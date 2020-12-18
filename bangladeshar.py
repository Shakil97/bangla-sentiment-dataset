import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

questionlist = []

def getQuestions(tag,page):
    url = f'http://www.bangladesherkhabor.net/{tag}?tab=Active&page={page}&pagesize=50'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'col-sm-18 photobox'})
    for item in questions:
        question = {
        'tag':tag,
        'title': item.find('div', {'class': 'more-details'}).text,
        #'link': 'https://stackoverflow.com' + item.find('a', {'class': 'question-hyperlink'})['href'],
        #'votes': int(item.find('span', {'class': 'vote-count-post'}).text),
        #'details': item.find('span', {'class': 'relativetime'})['title'],
        }
        questionlist.append(question)
    return
for x in range(1,40):
    getQuestions('football/27',x)
    getQuestions('cricket/28',x)
    getQuestions('Information%20Technology/96',x)
    getQuestions('social%20media/95',x)
    getQuestions('opinion/6',x)
    getQuestions('rangamela/10',x)
    getQuestions('Education/66',x)

df = pd.DataFrame(questionlist)
df.to_csv('bangladesh.csv', index=False)
print('Fin.')
