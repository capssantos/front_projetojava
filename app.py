from flask import Flask, request, session, redirect, url_for, render_template, flash, json, jsonify
from service.banco import Api
import json
from time import sleep
from random import *

app = Flask(__name__)
app.secret_key = b'TESTE'

api = Api()

@app.route('/')
def inicio():
    return render_template('index.html', data = api.allagencias())
#-------------------------------------------------------------
# START - AGENCIA - ROTAS E CONTROLLERS
@app.route('/agencia')
def allagencias():
    return render_template('all.html', data = api.allagencias(), page = 'agencia')

@app.route('/removeagencia/<id>')
def removeragencia(id):
    remove = api.removeragencia(id)
    if remove['msg'] == 'Agencia deletada com sucesso!':
        flash('Agencia deletada com sucesso!')
        
        return redirect(url_for('allagencias'))

@app.route('/cadastroagencia', methods=['GET', 'POST'])
def cadastroagencia():
    if request.method == 'POST':
        nomeagencia = request.form['nomeAgencia']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        new = api.registaragencia(nomeagencia, endereco, telefone)
        flash('Agencia ID:{idagencia}, cadastrada com sucesso!'.format(idagencia = new['idAgencia']))
        return redirect(url_for('allagencias'))

    return render_template('cadastro.html', page = 'agencia',
                                            nomeagencia = '',
                                            endereco = '',
                                            telefone = '',
                                            idagencia = '')

@app.route('/cadastroagencia/<id>', methods=['GET', 'POST'])
def alteraragencia(id):

    if request.method == 'GET':
        agencia = api.agencia(id)
        return render_template('cadastro.html', page = 'agencia',
                                                nomeagencia = agencia['nomeAgencia'],
                                                endereco = agencia['endereco'],
                                                telefone = agencia['telefone'],
                                                idagencia = agencia['idAgencia'])

    if request.method == 'POST':
        idagencia = request.form['idAgencia']
        nomeagencia = request.form['nomeAgencia']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        new = api.atualizaragencia(idagencia, nomeagencia, endereco, telefone)
        flash('Agencia ID:{idagencia}, autalizado com sucesso!'.format(idagencia = new['idAgencia']))
        return redirect(url_for('allagencias'))
# END - AGENCIA - ROTAS E CONTROLLERS
#-------------------------------------------------------------
# START - CLIENTE - ROTAS E CONTROLLERS
@app.route('/cliente')
def allcliente():
    return render_template('all.html', data = api.allclientes(), page = 'cliente')

@app.route('/removecliente/<id>')
def removercliente(id):
    remove = api.removercliente(id)
    print(remove)
    if remove['msg'] == 'Cliente deletado com sucesso!':
        flash('Cliente deletado com sucesso!')
        
        return redirect(url_for('allcliente'))

@app.route('/cadastrocliente', methods=['GET', 'POST'])
def cadastrocliente():
    if request.method == 'POST':
        clientenome = request.form['clienteNome']
        clientecpf = request.form['clienteCPF']
        clientefone = request.form['clienteFone']
        idagencia = request.form['idAgencia']
        
        conta = api.registarconta(idagencia, randrange(1000,10000,2), '0.0')

        idcontacorrente = conta['idContaCorrente']
        
        new = api.registarcliente(clientenome, clientecpf, clientefone, idcontacorrente, idagencia)
        flash('Cliente ID:{idagencia}, Conta Numero: {contaCorrenteNumero}, cadastrada com sucesso!'.format(idagencia = new['idCliente'], contaCorrenteNumero = conta['contaCorrenteNumero']))
        return redirect(url_for('allcliente'))

    return render_template('cadastro.html', page = 'cliente',
                                            clientenome = '',
                                            clientecpf = '',
                                            clientefone = '',
                                            idcontacorrente = '',
                                            idagencia = '',
                                            idcliente = ''
                                            )

@app.route('/cadastrocliente/<id>', methods=['GET', 'POST'])
def alterarcliente(id):

    if request.method == 'GET':
        cliente = api.cliente(id)
        conta = api.conta(str(cliente['idContaCorrente']))
        return render_template('cadastro.html', page = 'cliente',
                                                clientenome = cliente['clienteNome'],
                                                clientecpf = cliente['clienteCPF'],
                                                clientefone = cliente['clienteFone'],
                                                idcontacorrente = cliente['idContaCorrente'],
                                                idagencia = cliente['idAgencia'],
                                                idcliente = cliente['idCliente'],
                                                contacorrentenumero = conta['contaCorrenteNumero'],
                                                contacorrentesaldo = conta['contaCorrenteSaldo'],
                                                )

    if request.method == 'POST':
        idagencia = request.form['idAgencia']
        nomeagencia = request.form['nomeAgencia']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        new = api.atualizaragencia(idagencia, nomeagencia, endereco, telefone)
        flash('Agencia ID:{idagencia}, autalizado com sucesso!'.format(idagencia = new['idAgencia']))
        return redirect(url_for('allcliente'))
# END - CLIENTE - ROTAS E CONTROLLERS
#-------------------------------------------------------------
# START - CONTA - ROTAS E CONTROLLERS

# END - CONTA - ROTAS E CONTROLLERS
#-------------------------------------------------------------
# START - EXTRATO - ROTAS E CONTROLLERS

# END - EXTRATO - ROTAS E CONTROLLERS
#-------------------------------------------------------------
@app.errorhandler(404)
def error_404(e):
    return '<h1>No source like your request.</h1>', 404

if __name__ == '__main__':
    app.run(debug=True, port=7000)