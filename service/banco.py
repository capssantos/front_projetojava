import requests as req
import json

class Api(object):
    def __init__(self):
        self.url = 'https://backend-java.carlosp.dev/'
        # self.url = 'http://localhost:8080/'
        self.headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        # self.url = 'http://srv-captain--backend-java/'
    
    # START - AGENCIA - ROTAS E CONTROLLERS
    def allagencias(self):
        res = req.get(url=self.url+'allagencias')
        res = json.loads(res.text)
        return res

    def allagencia_id(self):
        res = req.get(url=self.url+'allagencias')
        res = json.loads(res.text)
        lista = []
        for i in res:
            lista.append(str(i['idAgencia'])+' - '+i['nomeAgencia'])
        return lista

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
    
    def agencia(self, id_agencia):
        res = req.get(url=self.url+'agencia/'+ id_agencia)
        res = json.loads(res.text)
        return res

    def atualizaragencia(self, idagencia, nomeagencia, endereco, telefone):
        query = '{ \"idAgencia\":%(idAgencia)s, \"nomeAgencia\":%(nomeagencia)s, \"endereco\": %(endereco)s, \"telefone\":%(telefone)s }' % {
            "idAgencia": json.dumps(idagencia),
            "nomeagencia": json.dumps(nomeagencia),
            "endereco": json.dumps(endereco),
            "telefone": json.dumps(telefone)
        }
        query = json.loads(query)
        res = req.put(url=self.url+'alteraragencia', json=query, headers=self.headers)
        res = json.loads(res.text)
        return res
    # END - AGENCIA - ROTAS E CONTROLLERS
    # START - CLIENTE - ROTAS E CONTROLLERS
    def allclientes(self):
        res = req.get(url=self.url+'allclientes')
        res = json.loads(res.text)
        return res

    def allcliente_id(self):
        res = req.get(url=self.url+'allclientes')
        res = json.loads(res.text)
        lista = []
        for i in res:
            conta = self.conta(str(i['idContaCorrente']))
            lista.append('ID Cliente: '+str(i['idCliente'])+' '+'000'+str(i['idAgencia'])+' '+str(conta['contaCorrenteNumero'])+' - 0 | Cliente: '+i['clienteNome'])
        return lista

    def removercliente(self, id):
        res = req.delete(url=self.url+'removercliente/'+id, headers=self.headers)
        res = json.loads(res.text)
        return res

    def registarcliente(self, clientenome, clientecpf, clientefone, idcontacorrente, idagencia):
        query = '{\"clienteCPF\": %(clientenome)s,\"clienteFone\": :%(clientefone)s,\"clienteNome\": %(clientenome)s,\"idAgencia\": {\"idAgencia\":%(idagencia)s},\"idContaCorrente\": {\"idAgencia\": {\"idAgencia\": %(idagencia)s},\"idContaCorrente\": %(idcontacorrente)s} }' % {
            "clientenome": json.dumps(clientenome),
            "clientecpf": json.dumps(clientecpf),
            "clientefone": json.dumps(clientefone),
            "idcontacorrente": json.dumps(idcontacorrente),
            "idagencia": json.dumps(idagencia)
        }
        query = json.loads(query)
        res = req.post(url=self.url+'cadastrarcliente', json=query, headers=self.headers)
        res = json.loads(res.text)
        return res

    def atualizarcliente(self, idcliente, clientenome, clientecpf, clientefone, idcontacorrente, idagencia):
        query = '{ \"idCliente\":%(idcliente)s, \"clienteNome\":%(clientenome)s, \"clienteCPF\": %(clientecpf)s, \"clienteFone\":%(clientefone)s, \"idContaCorrente\":%(idcontacorrente)s, \"idAgencia\":%(idagencia)s  }' % {
        "idcliente": json.dumps(idcliente),
        "clientenome": json.dumps(clientenome),
        "clientecpf": json.dumps(clientecpf),
        "clientefone": json.dumps(clientefone),
        "idcontacorrente": json.dumps(idcontacorrente),
        "idagencia": json.dumps(idagencia),
        "idagencia": json.dumps(idagencia)
        }
        query = json.loads(query)
        res = req.put(url=self.url+'alterarcliente', json=query, headers=self.headers)
        res = json.loads(res.text)
        return res

    def cliente(self, id_cliente):
        res = req.get(url=self.url+'cliente/'+ id_cliente)
        res = json.loads(res.text)
        return res


    # END - CLIENTE - ROTAS E CONTROLLERS
    # START - CONTA - ROTAS E CONTROLLERS
    def registarconta(self, idagencia, contacorrentenumero):
        query = '{\"contaCorrenteNumero\": %(contacorrentenumero)s, \"idAgencia\": {\"idAgencia\": %(idagencia)s},\"saldo\": 0}' % {
            "idagencia": json.dumps(idagencia),
            "contacorrentenumero": json.dumps(contacorrentenumero),
        }
        query = json.loads(query)
        res = req.post(url=self.url+'cadastratarconta', json=query, headers=self.headers)
        res = json.loads(res.text)
        return res

    def alterarconta(self, idcontacorrente, idagencia, contacorrentenumero, contacorrentesaldo):
        query = '{\"idContaCorrente\":%(idcontacorrente)s, \"idAgencia\":%(idagencia)s, \"contaCorrenteNumero\": %(contacorrentenumero)s, \"contaCorrenteSaldo\":%(contacorrentesaldo)s }' % {
            "idcontacorrente": json.dumps(idcontacorrente),
            "idagencia": json.dumps(idagencia),
            "contacorrentenumero": json.dumps(contacorrentenumero),
            "contacorrentesaldo": json.dumps(contacorrentesaldo)
        }
        query = json.loads(query)
        res = req.post(url=self.url+'cadastratarconta', json=query, headers=self.headers)
        res = json.loads(res.text)
        return res

    def conta(self, id_conta):
        res = req.get(url=self.url+'conta/'+ id_conta)
        res = json.loads(res.text)
        return res

    # END - CONTA - ROTAS E CONTROLLERS
    # START - EXTRATO - ROTAS E CONTROLLERS

    # END - EXTRATO - ROTAS E CONTROLLERS

    # START - FULL - ROTAS E CONTROLLERS



    # END - FULL - ROTAS E CONTROLLERS