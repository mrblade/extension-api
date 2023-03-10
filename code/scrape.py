import requests
import json
from bs4 import BeautifulSoup
r = requests.get('https://www.inshorts.com/en/read/')
res = []
soup = BeautifulSoup(r.content, 'html.parser')
content = soup.find_all('div', class_='news-card')
for el in content:
    title = el.select('.news-card-title .clickable span')[0].text
    time = el.select('.news-card-author-time-in-title .time')[0].text
    url = el.select('.read-more a')[0]['href'] if el.select('.read-more a') else "https://www.inshorts.com" + el.select('.news-card-title .clickable')[0]['href']
    res.append({'title': title.strip(), "url" : url.strip(), "time" : time.strip() })

with open("inshorts.json", 'w') as f:
    json.dump(res, f)
    print('Inshorts updated')
