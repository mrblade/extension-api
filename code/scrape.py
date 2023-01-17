import requests
import json
from bs4 import BeautifulSoup
import os
r = requests.get('https://www.inshorts.com/en/read/')
res = []
soup = BeautifulSoup(r.content, 'html.parser')
content = soup.find_all('div', class_='news-card')
mypath = os.path.abspath(os.curdir)
for el in content:
    title = el.select('.news-card-title .clickable span')[0].text
    time = el.select('.news-card-author-time-in-title .time')[0].text
    url = el.select('.read-more a')[0]['href'] if el.select('.read-more a') else "https://www.inshorts.com" + el.select('.news-card-title .clickable')[0]['href']
    res.append({'title': title.strip(), "url" : url.strip(), "time" : time.strip() })
#if not os.path.isdir(mypath):
   #os.makedirs(mypath)
mode = 'a' if os.path.exists(mypath) else 'w'
with open(mypath + '/inshorts.json', mode) as f:
    json.dump(res, f)
    print('Inshorts updated')