import json
import pytest
from app.cadastro import CadastroPessoas
from app.pessoa import Pessoa


# ===== TESTES DA CLASSE CADASTROPESSOAS =====

def test_adicionar_pessoa_simples():
    """Testa se uma pessoa é adicionada corretamente"""
    cadastro = CadastroPessoas()
    cadastro.adicionar_pessoa("Gabriel", 26)
    
    assert len(cadastro.pessoas) == 1
    assert cadastro.pessoas[0].nome == "Gabriel"
    assert cadastro.pessoas[0].idade == 26


def test_adicionar_multiplas_pessoas():
    """Testa adição de múltiplas pessoas"""
    cadastro = CadastroPessoas()
    cadastro.adicionar_pessoa("Gabriel", 26)
    cadastro.adicionar_pessoa("Luiz", 22)
    cadastro.adicionar_pessoa("Maria", 30)
    
    assert len(cadastro.pessoas) == 3
    assert cadastro.pessoas[1].nome == "Luiz"
    assert cadastro.pessoas[2].idade == 30


def test_cadastro_vazio_inicialmente():
    """Testa se cadastro é criado vazio"""
    cadastro = CadastroPessoas()
    assert len(cadastro.pessoas) == 0
    assert cadastro.pessoas == []


# ===== TESTES DO JSON =====

def test_json_lista_vazia():
    """Testa se JSON de lista vazia é '[]'"""
    cadastro = CadastroPessoas()
    resultado = cadastro.listar_json()
    
    assert resultado == "[]"
    assert json.loads(resultado) == []


def test_json_uma_pessoa():
    """Testa se JSON de uma pessoa é formatado corretamente"""
    cadastro = CadastroPessoas()
    cadastro.adicionar_pessoa("Gabriel", 26)
    
    resultado = cadastro.listar_json()
    dados = json.loads(resultado)
    
    assert len(dados) == 1
    assert dados[0]["nome"] == "Gabriel"
    assert dados[0]["idade"] == 26


def test_json_multiplas_pessoas():
    """Testa se JSON de múltiplas pessoas é formatado corretamente"""
    cadastro = CadastroPessoas()
    cadastro.adicionar_pessoa("Ana", 25)
    cadastro.adicionar_pessoa("Bruno", 30)
    
    resultado = cadastro.listar_json()
    dados = json.loads(resultado)
    
    assert len(dados) == 2
    assert dados[0]["nome"] == "Ana"
    assert dados[1]["nome"] == "Bruno"


def test_json_valido():
    """Testa se o JSON retornado é válido"""
    cadastro = CadastroPessoas()
    cadastro.adicionar_pessoa("Test", 20)
    
    resultado = cadastro.listar_json()
    
    # Não deve lançar exceção
    dados = json.loads(resultado)
    assert isinstance(dados, list)


# ===== TESTES DA CLASSE PESSOA =====

def test_pessoa_criacao_valida():
    """Testa criação válida de uma pessoa"""
    pessoa = Pessoa("Carlos", 40)
    
    assert pessoa.nome == "Carlos"
    assert pessoa.idade == 40


def test_pessoa_nome_com_espacos_extra():
    """Testa se espaços extras no nome são removidos"""
    pessoa = Pessoa("  Ana Silva  ", 25)
    
    assert pessoa.nome == "Ana Silva"


def test_pessoa_nome_vazio_erro():
    """Testa se nome vazio lança ValueError"""
    with pytest.raises(ValueError):
        Pessoa("", 25)


def test_pessoa_nome_so_espacos_erro():
    """Testa se nome com apenas espaços lança ValueError"""
    with pytest.raises(ValueError):
        Pessoa("   ", 25)


def test_pessoa_nome_nao_string_erro():
    """Testa se nome não-string lança ValueError"""
    with pytest.raises(ValueError):
        Pessoa(123, 25)


def test_pessoa_idade_negativa_erro():
    """Testa se idade negativa lança ValueError"""
    with pytest.raises(ValueError):
        Pessoa("Paulo", -5)


def test_pessoa_idade_zero_valida():
    """Testa se idade zero é aceita"""
    pessoa = Pessoa("Bebê", 0)
    
    assert pessoLucas", 25.5)


def test_pessoa_tance(resultado, dict)
    assert resultado["nome"] == "Felipe"
    assert resultado["idade"] == 35
    assert len(resultado) == 2


def test_pessoa_idade_grande():
    """Testa se idades grandes são aceitas"""
    pessoa = Pessoa("Methuselah", 969)
    