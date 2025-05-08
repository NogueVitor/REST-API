import json
import os

arquivo_de_personagens = 'personagens_db.json'

caminho_completo = os.path.join(os.path.dirname(__file__), arquivo_de_personagens)

def carregar_personagens():
    try:
        with open(caminho_completo, 'r') as arquivo:
            return json.load(arquivo)
    except:
        return []

def save_personagens(lista_de_personagens):
    with open(caminho_completo, 'w') as arquivo:
        json.dump(lista_de_personagens, arquivo, indent=2)

Personagens = carregar_personagens()

'''Aqui é tipo um "backup" para caso o arquivo .json for apagado ou dar algum problema com lista vazia. Aí o if not vai ser ativado
e carregar os dados padrôes que coloquei no dicionário.'''
if not Personagens:
    Personagens = [
    {"id": 1, "nome": "Lohse", "classe": "Encantadora", "raca": "Humana", "origem": "Cantora Itinerante", "idade": 28, "afiliacao": "Ordem da Fonte"},
    {"id": 2, "nome": "Ifan ben-Mezd", "classe": "Caçador de Recompensas", "raca": "Humano", "origem": "Mercenário", "idade": 35, "afiliacao": "Lucian the Divine"},
    {"id": 3, "nome": "Fane", "classe": "Feiticeiro", "raca": "Esqueleto Eterno", "origem": "Arqueólogo", "idade": "Desconhecida (milênios)", "afiliacao": "Sétimo Senhor"},
    {"id": 4, "nome": "Beast", "classe": "Ladino", "raca": "Anão", "origem": "Pirata", "idade": 42, "afiliacao": "Rainha Justinia"},
    {"id": 5, "nome": "Red Prince", "classe": "Guerreiro", "raca": "Lizarman", "origem": "Nobre Exilado", "idade": 31, "afiliacao": "Império dos Lizarmas"},
    {"id": 6, "nome": "Sebille", "classe": "Assassina", "raca": "Elfa", "origem": "Escrava Fugitiva", "idade": 89, "afiliacao": "Scion of Shadow"}
]
    save_personagens(Personagens)
