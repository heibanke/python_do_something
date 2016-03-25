import requests

r = requests.get('https://api.github.com/events')
r.json()
r.encoding
r.text

r = requests.get('https://www.github.com')
r.url
r.history


r = requests.get('https://www.github.com', allow_redirects=False)

requests.get('https://www.github.com', timeout=0.001)


url = "http://www.heibanke.com/lesson/crawler_ex01/"
params = {'username':'heibanke','password': '10'}
r = requests.post(url,data=params)

