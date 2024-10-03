from pickle import GET
import requests
from flask import Flask, render_template, request, redirect
lista=[]

app = Flask(__name__)


API_KEY = 'live_9IkiEHbyniMDRpkoRnQ0zNtZp0xB1eC2t9qznlgEbnBAaghnKahekVwdBT51iOr9'
BASE_URL = 'https://api.thecatapi.com/v1/images/search'


@app.route('/')
def hello_world():
    return render_template("Home.html", Titulo="Bem vindo ao site de Gatos")

@app.route('/gatos')
def gatos():
    return render_template("Gatos.html", Selva="Melhores Gatos")

@app.route('/sobre')
def sobre():
    return render_template("Sobre.html", Selva2="Sobre nosso site")

@app.route('/cadastro')
def cadastro():
    return render_template("Cadastro.html", Titulo="Cadastro de Gatos")

@app.route('/exibir')
def exibir():
    return render_template("Exibir.html", Titulo="Gatos Cadastrados", lista=lista)

@app.route('/criar',methods=['POST'])
def criar():
    numero = request.form['numero']
    nome = request.form['nome']
    tipo = request.form['tipo']
    altura = request.form['altura']
    peso = request.form['peso']
    acesso = {'x-api-key': API_KEY}
    solicitacao = requests.get(BASE_URL, headers=acesso)
    dados = solicitacao.json()
    imagemdogato = dados[0]['url']
    animal = [numero, nome, tipo, altura, peso,imagemdogato]
    lista.append(animal)
    return redirect('/exibir')

if __name__ == '__main__':

    app.run()
