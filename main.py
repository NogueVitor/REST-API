from flask import Flask , make_response , jsonify, request
from bd import Personagens, save_personagens

app = Flask(__name__)

def ID_mais_um():
    if not Personagens:
        return 1
    return max(personagem['id'] for personagem in Personagens) + 1
    '''Sempre que eu fazer um POST, o ID do meu novo personagem vai ser baseado pelo maior + 1.
    Achei essa solução mais simples do que procurar o anterior e somar com 1, afinal,
    eu teria que tratar os casos em que o anterior não fosse o maior ID do db.'''


@app.route('/personagens', methods=['GET'])
def get_personagens():
    return make_response (
        jsonify(Lista_de_personagens = Personagens)
    )

@app.route('/personagens/<int:personagem_id>', methods=['GET'])
def get_personagem(personagem_id):
    personagem_encontrado = None
    
    for personagem in Personagens:
        if personagem['id'] == personagem_id:
            personagem_encontrado = personagem
            break
    if personagem_encontrado is not None:
        resposta = make_response(
            jsonify(personagem_encontrado),
            200  # Status OK
        )
        return resposta
    
    resposta_erro = {
        "mensagem": f"Personagem com ID {personagem_id} nao encontrado"
    }
    
    return make_response(
        jsonify(resposta_erro),
    )


@app.route('/personagens', methods=['POST'])
def create_personagem():
    personagem = request.json

    personagem['id'] = ID_mais_um()
    Personagens.append(personagem)

    save_personagens(Personagens)
    
    return make_response(
        jsonify(
            mensagem='Personagem registrado com sucesso.',
            dados=personagem
        )
    )

''' O GET e o POST são bem simples e foram tranquilos de fazer.
Já o mais chatinho foi mesmo o DELETE, por causa dele precisar realmente de alguns tratamentos para funcionar direito.'''

@app.route('/personagens/<int:personagem_id>', methods=['DELETE'])
def delete_personagem(personagem_id):
    personagem_encontrado = None
    for personagem in Personagens:
        if personagem['id'] == personagem_id:
            personagem_encontrado = personagem
            break
    if personagem_encontrado is None:
        resposta_erro = {
            "status": "erro",
            "mensagem": f"Nao foi encontrado um personagem com o ID {personagem_id}"}
        return make_response(jsonify(resposta_erro))

    Personagens.remove(personagem_encontrado)
    save_personagens(Personagens)

    resposta_sucesso = {
        "mensagem": "Personagem removido do banco de dados.",
        "dados": personagem_encontrado,
        "total_personagens_restantes": len(Personagens)
    }

    return make_response(
        jsonify(resposta_sucesso)
        )


app.run()