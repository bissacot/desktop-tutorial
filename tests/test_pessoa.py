import pytest
from app.pessoa import Pessoa

def test_criacao_valida():
    pessoa = Pessoa("Luiz", 30)
    assert pessoa.nome == "Luiz"
    assert pessoa.idade == 30

def test_nome_vazio():
    with pytest.raises(ValueError):
        Pessoa("", 20)

def test_nome_espaco():
    with pytest.raises(ValueError):
        Pessoa("   ", 20)

def test_idade_negativa():
    with pytest.raises(ValueError):
        Pessoa("Gabriel", -1)

def test_idade_zero():
    pessoa = Pessoa("Gabriel", 0)
    assert pessoa.idade == 0

def test_nome_com_espacos_laterais():
    pessoa = Pessoa("  Gabriel  ", 25)
    assert pessoa.nome == "Gabriel"

def test_nome_tipo_errado():
    with pytest.raises(ValueError):
        Pessoa(123, 20)

def test_idade_tipo_errado():
    with pytest.raises(ValueError):
        Pessoa("Gabriel", "vinte")

def test_to_dict():
    pessoa = Pessoa("Ana", 22)
    d = pessoa.to_dict()
    assert d == {"nome": "Ana", "idade": 22}

def test_nome_maiusculo_minusculo():
    pessoa = Pessoa("ana", 22)
    assert pessoa.nome == "ana"

def test_idade_grande():
    pessoa = Pessoa("Carlos", 120)
    assert pessoa.idade == 120

def test_nome_com_caracteres_especiais():
    pessoa = Pessoa("João da Silva!", 40)
    assert pessoa.nome == "João da Silva!"

def test_idade_limite():
    pessoa = Pessoa("Maria", 150)
    assert pessoa.idade == 150

def test_nome_unicode():
    pessoa = Pessoa("José Álvares", 50)
    assert pessoa.nome == "José Álvares"

def test_idade_extremamente_alta():
    pessoa = Pessoa("Matusalém", 969)
    assert pessoa.idade == 969