# pesquisa-simples

Um pequeno projeto em Flask para praticar um algoritmo de pesquisa em listas ou conjuntos de dados.
---
##  Sobre

Este projeto foi desenvolvido para treinar os conceitos de:
- Flask (framework web em Python).
- Renderização com **templates** (HTML).
- Estrutura típica de aplicação web:
  - `manage.py`.
  - pastas `templates/`, `static/css/`, `dados/`.
- Lógica de busca simples baseada em entrada de usuário.
---
##  Funcionalidades

- Campo de busca simples em uma lista de itens (o que estiver em `dados/`).
- Interface minimalista em HTML com estilização em CSS.
- Exibição dos resultados da busca na mesma página.
---
##  Tecnologias Utilizadas

- Python + Flask
- HTML (templates Jinja2)
- CSS para estilização básica
- Estrutura de diretórios (`templates/`, `static/`, `dados/`)
---
## estrutura do projeto

- pesquisa-simples/
- │
- ├── manage.py         # Ponto de entrada da aplicação Flask
- ├── dados/            # Dados usados para busca (por exemplo: lista de nomes)
- ├── templates/
- │   ├── base.html     # Template base
- │   └── index.html    # Página principal com campo de busca e resultados
- │
- └── static/
-     └── css/
-       └── style.css # Estilização básica da interface
