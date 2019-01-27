import requests as req


class JokePi:
    def __init__(self, Index, UID, URL):
        self.Index = Index
        self.UID = UID
        self.URL = URL

    def getJsonByIndex(self):
        r = req.get(self.URL + self.UID)
        print(r.json()[self.Index])

    def getJson(self):
        r = req.get(self.URL + self.UID)
        print(r.json())

    def updatePlotData(self,plotName,x,y):
        r = req.post(self.URL + self.UID+ '/' + plotName + '/' + x + '/' + y )
        data = r.text
        print(data)

    def testPost(self):
        r = req.post(self.URL + self.UID + '/Plots')
        data = r.text
        print(data)

