from flask import Blueprint, jsonify, request
from ..models import Cliente
from ..extensions import db
from sqlalchemy import desc

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/', methods=['GET'])
def get_clientes():
    # Obtém o parâmetro de consulta 'codigo'
    item_codigo = request.args.get('codigo')
    if item_codigo:
        cliente = Cliente.query.get_or_404(item_codigo)
        return jsonify({'codigo': cliente.codigo, 'razao': cliente.razao, 'email': cliente.email})
    else:
        clientes = Cliente.query.order_by(desc(Cliente.codigo)).limit(25).all()
        return jsonify([{'codigo': cliente.codigo, 'razao': cliente.razao, 'email': cliente.email} for cliente in clientes])

@cliente_bp.route('/', methods=['POST'])
def add_cliente():
    data = request.get_json()
    new_cliente = Cliente(codigo=data['codigo'], razao=data['razao'], email=data['email'])
    db.session.add(new_cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente criado com sucesso'}), 201

@cliente_bp.route('/', methods=['PUT'])
def update_cliente():
    item_id = request.args.get('codigo')
    if not item_id:
        return jsonify({'message': 'Código não informado'}), 400

    try:
        item_id = int(item_id)
    except ValueError:
        return jsonify({'message': 'Código deve ser um número inteiro'}), 400

    if item_id:
        cliente = Cliente.query.get_or_404(item_id)
        #Obtém os dados do corpo da requisição
        data = request.get_json()
        cliente.codigo = data['codigo']
        cliente.razao = data['razao']
        cliente.email = data['email']
        db.session.commit()
        return jsonify({'message': 'Cliente atualizado com sucesso'})

@cliente_bp.route('/', methods=['DELETE'])
def delete_cliente():
    item_id = request.args.get('codigo')
    if not item_id:
        return jsonify({'message': 'Código não informado'}), 400

    try:
        item_id = int(item_id)
    except ValueError:
        return jsonify({'message': 'Código deve ser um número inteiro'}), 400

    if item_id:
        cliente = Cliente.query.get_or_404(item_id)
        db.session.delete(cliente)
        db.session.commit()
        return jsonify({'message': 'Cliente excluído com sucesso'})
