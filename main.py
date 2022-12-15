from flask import Flask, request, session, redirect, url_for, render_template, flash, json, jsonify
from service.banco import Api
import json

main = Flask(__name__)
api = Api()

@main.route('/')
def inicio():
    data = api.allagencias()
    return render_template('index.html', data = data)

@main.route('/agencia')
def allagencias():
    data = api.allagencias()
    return render_template('agencias.html', data = data)

if __name__ == '__main__':
    main.run(debug=True, port=7000)