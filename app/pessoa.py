class Pessoa:
	def __init__(self, nome: str, idade: int):
		self.nome = nome
		self.idade = idade

	def to_dict(self):
		return {"nome": self.nome, "idade": self.idade}
