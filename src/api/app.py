from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

pedidos = []

@app.route('/pedidos', methods=['GET'])
def get_requests():
    return jsonify(pedidos)

@app.route('/novo', methods=['POST'])
def add_request():
    data = request.get_json()
    if not data or 'usuario' not in data or 'email'not in data or 'descricao' not in data:
        return make_response(jsonify({"message": "os campos: usuario, email e descricao sao obrigatorios"}), 400)
    pedido_id = len(pedidos) + 1
    data['id'] = pedido_id
    pedidos.append(data)
    return make_response(jsonify(data), 201)

@app.route('/pedido/<int:pedido_id>', methods=['GET'])
def get_request(pedido_id):
    pedido = next((pedido for pedido in pedidos if pedido['id']==pedido_id), None)
    if pedido:
        return jsonify(pedido)
    else:
        return make_response(jsonify({"message":"Pedido não encontrado"}), 404)


@app.route('/pedido/<int:pedido_id>', methods=['PUT'])
def update_request(pedido_id):
    pedido = next((pedido for pedido in pedidos if pedido['id']==pedido_id), None)
    if pedido:
        data = request.get_json()
        pedido.update(data)
        return jsonify(pedido)
    else:
        return make_response(jsonify({"message": "Pedido não encontrado"}), 404)
    
@app.route('/pedido/<int:pedido_id>', methods=['DELETE'])
def delete_pedido(pedido_id):
    global pedidos
    pedido = next((pedido for pedido in pedidos if pedido['id']==pedido_id), None)
    if pedido:
        pedidos = [pedido for pedido in pedidos if pedido['id']!=pedido_id]
        return make_response(jsonify({"message":"pedido deletado!"}), 200)
    else:
        return make_response(jsonify({"message":"pedido não encontrado"}), 404)
    
if __name__ == '__main__':
    app.run(debug=True, threaded=False)