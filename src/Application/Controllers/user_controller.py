from flask import make_response, jsonify, request
from Service.user_service import save

def store():
    usuario = request.json
    if not isinstance(usuario.get('senha'), str):
        return make_response(
            jsonify(
                {'mensagem': 'Senha deve ser uma string'}
                ), 400
            )
    
    save(usuario)
    return make_response(
        jsonify(
            {'mensagem': 'Cadastro salvo com sucesso'}
            ), 201
        )