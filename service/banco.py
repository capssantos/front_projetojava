import requests as req
import json

class Api(object):
    def __init__(self):
        # self.url = 'https://backend-java.carlosp.dev/'
        self.url = 'http://srv-captain--backend-java/'
    
    def allagencias(self):
        res = req.get(url=self.url+'allagencias')
        res = json.loads(res.text)
        return res