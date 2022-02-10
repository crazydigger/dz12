import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://api.hh.ru/vacancies'
params = {'text': 'Python developer',
'page': 1}
result = requests.get(url, params=params, verify=False).json()
items=result['items']
first = items[0]

print('URL:::::::::::::::::::',first['url'])
print('len',len(items),items[0])

print(':::::::::::::::::::::::::::::::',result)