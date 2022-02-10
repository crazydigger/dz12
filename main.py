import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://api.hh.ru/vacancies'
params = {'text': 'java developer',
'page': 1}
result = requests.get(url, params=params, verify=False).json()

print(':::::::::::::::::::::::::::::::',result)