class Pessoa:
	def __init__(self, nome: str, idade: int):
		if not isinstance(nome, str) or not nome.strip():
			raise ValueError("Nome não pode ser vazio ou só espaços.")
		if not isinstance(idade, int) or idade < 0:
			raise ValueError("Idade deve ser um inteiro não negativo.")
		self.nome = nome.strip()
		self.idade = idade

	def to_dict(self):
		return {"nome": self.nome, "idade": self.idade}
