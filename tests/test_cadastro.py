from app.cadastro import CadastroPessoas


def test_adicionar_pessoa():
    cadastro = CadastroPessoas()
    cadastro.adicionar_pessoa("Gabriel", 26)

    assert len(cadastro.pessoas) == 2


def test_json_saida():
    cadastro = CadastroPessoas()
    cadastro.adicionar_pessoa("Gabriel", 26)

    resultado = cadastro.listar_json()

    assert "Gabriel" in resultado