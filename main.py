import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://api.hh.ru/vacancies'
params = {'text': 'Python developer',
'page': 1,
'array':1,
'User-Agent': 'api-test-agent'}
result = requests.get(url, params=params, verify=False).json()
items=result['items']
first = items[0]
req=first['snippet']
print('URL:::::::::::::::::::',req)
print('len',len(items),items[0])
reqs=[]
for i in first['snippet']:
    r =i['snippet']
    for j in r:
        print(r,'Требования!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',j)
        reqs.append(j)
print('Требования:::::::::::::::::::::::::::::::',reqs)