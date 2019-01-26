import requests as req

URL = 'https://nameless-falls-40724.herokuapp.com/'

r=req.get(URL)

data=r.json()

print(data)