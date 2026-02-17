import requests

url = 'https://api.github.com/users/'
url_sufix = '/events'

username = input()

response = requests.get(url + username + url_sufix)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')
