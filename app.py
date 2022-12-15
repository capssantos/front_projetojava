from flask import Flask, request, session, redirect, url_for, render_template, flash, json, jsonify
from service.banco import Api
import json

app = Flask(__name__)
api = Api()

@app.route('/')
def inicio():
    data = api.allagencias()
    return render_template('index.html', data = data)

@app.route('/agencia')
def allagencias():
    data = api.allagencias()
    return render_template('agencias.html', data = data)

@app.errorhandler(404)
def error_404(e):
    return '<h1>No source like your request.</h1>', 404

if __name__ == '__main__':
    app.run(debug=True, port=5555)