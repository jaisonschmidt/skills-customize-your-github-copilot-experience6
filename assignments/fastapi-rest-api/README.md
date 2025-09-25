# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprender a criar uma API REST simples utilizando o framework FastAPI em Python. O estudante irá construir endpoints para manipular recursos, praticando conceitos de rotas, métodos HTTP e respostas JSON.

## 📝 Tasks

### 🛠️ Criar Estrutura Básica da API

#### Description
Inicie um novo projeto FastAPI e crie um arquivo principal (`main.py`). Implemente um endpoint GET simples que retorna uma mensagem de boas-vindas.

#### Requirements
Completed program should:

- Inicializar um app FastAPI
- Criar endpoint GET `/` que retorna um JSON com uma mensagem de boas-vindas
- Rodar localmente usando Uvicorn

### 🛠️ CRUD para Recurso "Item"

#### Description
Implemente endpoints para criar, ler, atualizar e deletar itens (CRUD) usando FastAPI. Cada item deve ter um `id`, `nome` e `preco`.

#### Requirements
Completed program should:

- Endpoint POST `/items/` para criar um novo item
- Endpoint GET `/items/{id}` para buscar um item pelo id
- Endpoint PUT `/items/{id}` para atualizar um item existente
- Endpoint DELETE `/items/{id}` para remover um item
- Utilizar dicionário em memória para armazenar os itens
- Retornar respostas apropriadas em JSON
