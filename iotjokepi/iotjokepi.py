import requests as req


class JokePi:
    def __init__(self, Index, UID, URL):
        self.Index = Index
        self.UID = UID
        self.URL = URL

    def getJsonByIndex(self):
        r = req.get(self.URL + self.UID)
        return (r.json()[self.Index])

    def getJson(self):
        r = req.get(self.URL + self.UID)
        return r.json()

    def updatePlotData(self, plotName, x, y):
        r = req.post(self.URL + self.UID + '/' + plotName + '/' + x + '/' + y)
        data = r.text
        return data

    def getSwitchState(self, name):
        r = req.get(self.URL + self.UID + '/' + name)
        data = r.text
        return data

    def updateString(self,value):
        r = req.post(self.URL + self.UID + '/' + value)
        data = r.text
        return data

    def getString(self):
        r = req.get(self.URL + self.UID)
        data = r.text
        return data