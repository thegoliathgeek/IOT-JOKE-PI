import requests as req


class JokePi:
    def __init__(self, Index, UID, URL):
        self.Index = Index
        self.UID = UID
        self.URL = URL

    def getjson(self):
        r = req.get(self.URL)
        print(r.json()[self.Index])
