import requests as req

apiKey = ''
url = 'https://iotjokepi-pi.herokuapp.com'


def wakeServer():
    r = req.get(url + '/api/users/' + apiKey)
    d = r.json()
    print(d)


if __name__ == '__main__':
    wakeServer()
