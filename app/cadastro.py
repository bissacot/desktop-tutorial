import json
from app.pessoa import Pessoa


class CadastroPessoas:
    def __init__(self):
        self.pessoas = []

    def adicionar_pessoa(self, nome: str, idade: int):
        pessoa = Pessoa(nome, idade)
        self.pessoas.append(pessoa)

    def listar_json(self):
        return json.dumps([p.to_dict() for p in self.pessoas], ensure_ascii=False)