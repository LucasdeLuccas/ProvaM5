from flask import Flask, render_template, request, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('caminhos.json')

@app.route('/novo', methods=['POST'])
def novo_caminho():
    data = request.json
    db.insert(data)
    return jsonify({'message': 'Caminho cadastrado com sucesso'})

@app.route('/pegar_caminho/<int:id>', methods=['GET'])
def pegar_caminho(id):
    caminho = db.get(doc_id=id)
    if caminho:
        return jsonify(caminho)
    else:
        return jsonify({'error': 'Caminho não encontrado'})

@app.route('/listas_caminhos', methods=['GET'])
def listas_caminhos():
    caminhos = db.all()
    return jsonify(caminhos)

@app.route('/atualizar/<int:id>', methods=['PUT'])
def atualizar_caminho(id):
    data = request.json
    db.update(data, doc_ids=[id])
    return jsonify({'message': 'Caminho atualizado com sucesso'})

@app.route('/deletar/<int:id>', methods=['DELETE'])
def deletar_caminho(id):
    db.remove(doc_ids=[id])
    return jsonify({'message': 'Caminho deletado com sucesso'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
