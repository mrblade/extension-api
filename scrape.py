import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.inshorts.com/en/read/')
res = []
soup = BeautifulSoup(r.content, 'html.parser')
content = soup.find_all('div', class_='news-card')
for el in content:
    title = el.select('.news-card-title .clickable span')
    time = el.select('.news-card-author-time-in-title .time')
    url = el.select('.read-more a') or el.select('.news-card-title .clickable')
    res.append({'title': title[0].text, "url" : url[0]['href'], "time" : time[0].text })
print(res)