import requests
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://api.hh.ru/vacancies'
params = {'text': 'Python developer',
          'page': 1,
          'array': 1,
          'User-Agent': 'api-test-agent'}
result = requests.get(url, params=params, verify=False).json()
items = result['items']
first = items[0]
req = first['snippet']
req=str(req).replace('<','')
req=req.replace(':','')
req = str(req).split(',')

print('URL:::::::::::::::::::', str(req).split(','))
print('len', len(items), items[0])
reqs = []
for w in str(first['snippet']).split():
    r = str(w)
    for j in r:
        print(w, 'Требования',w,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', j)
        reqs.append(w)
print('Требования:::::::::::::::::::::::::::::::', reqs)
with open('data.json', 'w') as f:
    json.dump(reqs, f)
