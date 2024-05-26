import requests
url = 'http://localhost:3211/'
r = requests.get(url)
print(r.json())
