import requests as req
import json

class Api(object):
    def __init__(self):
        self.url = 'https://backend-java.carlosp.dev/'
        # self.url = 'http://localhost:8080/'
        self.headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        # self.url = 'http://srv-captain--backend-java/'
    
    def allagencias(self):
        res = req.get(url=self.url+'allagencias')
        res = json.loads(res.text)
        return res

    def removeragencia(self, id):
        res = req.delete(url=self.url+'removeragencia/'+id, headers=self.headers)
        res = json.loads(res.text)
        return res

    def registaragencia(self, nomeagencia, endereco, telefone):
        query = '{\"nomeAgencia\":%(nomeagencia)s, \"endereco\": %(endereco)s, \"telefone\":%(telefone)s }' % {
            "nomeagencia": json.dumps(nomeagencia),
            "endereco": json.dumps(endereco),
            "telefone": json.dumps(telefone)
        }
        query = json.loads(query)
        res = req.post(url=self.url+'cadastraragencia', json=query, headers=self.headers)
        res = json.loads(res.text)
        return res
        