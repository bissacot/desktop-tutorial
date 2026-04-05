# desktop-tutorial

[![CI/CD Status](https://github.com/seu-usuario/desktop-tutorial/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/seu-usuario/desktop-tutorial/actions/workflows/ci-cd.yml)

Projeto de exemplo para organização de um sistema desktop em Python.

## Estrutura do Projeto

```
desktop-tutorial/
├── app/
│   ├── __init__.py
│   ├── cadastro.py
│   ├── main.py
│   └── pessoa.py
├── tests/
│   ├── __init__.py
│   └── test_pessoa.py
├── requirements.txt
└── README.md
```

## Descrição
Este projeto serve como base para um sistema desktop em Python, com separação de módulos para cadastro, lógica principal e testes.

## Como usar
1. Clone o repositório:
	```bash
	git clone https://github.com/seu-usuario/desktop-tutorial.git
	```
2. Instale as dependências (adicione-as no requirements.txt conforme necessário):
	```bash
	pip install -r requirements.txt
	```
3. Implemente as funcionalidades nos arquivos dentro da pasta `app/`.
4. Escreva e execute os testes em `tests/`.

## Testes
Para rodar os testes (exemplo usando pytest):
```bash
pytest tests/
```

## CI/CD

Este projeto utiliza GitHub Actions para pipeline de CI/CD, incluindo:
- Execução automática de testes unitários
- Build do pacote
- Deploy simbólico (ajuste conforme sua estratégia)
- Notificação por e-mail (usando secret)
- Armazenamento de artifacts (relatório de testes e build)

## Dependências
- Python 3.11+
- pytest (adicione ao requirements.txt)

## .gitignore
Inclua padrões como:
- __pycache__/
- *.pyc
- dist/
- .env

## Prompts de IA utilizados
- "faça o readme.md"
- "faça o pipeline"
- "coloque meu cadastro no teste_cadastro, meu nome é Luiz"
- "atualiza o readme por favor"

## Observações
- O deploy está simbólico, ajuste conforme a estratégia do grupo (GitHub Releases, Docker, etc).
- O e-mail de notificação é configurado via secret no GitHub.
- Para cobertura de testes, adicione pytest-cov e configure o badge se desejar.

---

Projeto desenvolvido para a disciplina de DevOps/C214.
