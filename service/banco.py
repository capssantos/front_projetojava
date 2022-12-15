import psycopg2
import requests as req
import json

class Api(object):
    def __init__(self):
        # self.con = psycopg2.connect(host='mysql-db.carlosp.dev', database='agbank', user='root', password='1123581321')
        # self.url = 'https://backend-java.carlosp.dev/'
        self.url = 'http://srv-captain--backend-java/'
    
    def allagencias(self):
        res = req.get(url=self.url+'allagencias')
        res = json.loads(res.text)
        return res