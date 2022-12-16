from flask import Flask, request, session, redirect, url_for, render_template, flash, json, jsonify
from service.banco import Api
import json
from time import sleep

app = Flask(__name__)
app.secret_key = b'TESTE'

api = Api()

@app.route('/')
def inicio():
    return render_template('index.html', data = api.allagencias())

@app.route('/agencia')
def allagencias():
    return render_template('agencias.html', data = api.allagencias())

@app.route('/removeagencia/<id>')
def removeragencia(id):
    remove = api.removeragencia(id)
    if remove['msg'] == 'Agencia deletada com sucesso!':
        sleep(5)
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

    return render_template('cadastraragencia.html')

@app.errorhandler(404)
def error_404(e):
    return '<h1>No source like your request.</h1>', 404

if __name__ == '__main__':
    app.run(debug=True, port=7000)