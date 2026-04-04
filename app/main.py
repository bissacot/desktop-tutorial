from app.cadastro import CadastroPessoas


def executar():
    cadastro = CadastroPessoas()

    while True:
        nome = input("Digite o nome (ou FIM para encerrar): ").strip()

        if nome.upper() == "FIM":
            break

        try:
            idade = int(input("Digite a idade: "))
            cadastro.adicionar_pessoa(nome, idade)
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    print("JSON final:")
    print(cadastro.listar_json())


if name == "main":
    executar()