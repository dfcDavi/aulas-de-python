#uso da biblioteca flask (na verdade é um framework: conjunto de várias bibliotecas 
# que trabalham juntas para te dar uma estrutura mais sólida para desenvolver sua solução)

from flask import Flask, render_template

#criando a aplicação em flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1> Olá Mundo</h1><br><a href = '/sobre'>Página Sobre</a>"

@app.route('/sobre')
def sobre():
    return "<h3>Feito por Davi</h3><br><a href='/'>Página Inicial</a>"

@app.route('/nome/<nome>')
def saudacao(nome) :
    return f'<h1> Olá, {nome}!</h1>'

#iniciar o servidor
if __name__ == '__main__' :
    app.run(debug=True)

