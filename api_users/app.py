from flask import request, jsonify
from init import app, auth
from business import insert, getWebsites, getDetails, search


@app.route('/')
def index():
    return app.send_static_file('index.html')


# Carregando a saida da URL https://jsonplaceholder.typicode.com/users
@app.route('/users', methods=['POST'])
def insertUsers():
    return jsonify( insert(request.get_json()) )


# Os websites de todos os usuários
@app.route('/users/websites', methods=['GET'])
def getUsersWebsites():
    return jsonify( getWebsites() )


# O Nome, email e a empresa em que trabalha (em ordem alfabética)
@app.route('/users/detail', methods=['GET'])
def getUsersDetail():
    return jsonify( getDetails() )


# Mostrar todos os usuarios que contenham determinado texto no nome.
@app.route('/users/name/<string:name>', methods=['GET'])
def getUsers(name):
    return jsonify( search(name) )


@app.route('/users/status', methods=['GET'])
def getStatus():
    return jsonify( { "status": "its work!" } )


app.run(host='0.0.0.0', port=5050, debug =True)