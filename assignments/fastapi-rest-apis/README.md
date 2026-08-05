# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprender a construir uma API REST com FastAPI, aplicando rotas HTTP, validação de dados com Pydantic e respostas de erro adequadas.

## 📝 Tasks

### 🛠️ Criar Estrutura Base da API

#### Descrição
Implemente a estrutura inicial de uma aplicação FastAPI para gerenciar uma lista de tarefas (to-do) em memória.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI em `starter-code.py`.
- Definir um endpoint `GET /health` que retorne um status simples (por exemplo: `{ "status": "ok" }`).
- Definir um endpoint `GET /tasks` que retorne a lista de tarefas atual.
- Usar uma lista em memória para armazenar tarefas durante a execução.

### 🛠️ Implementar CRUD com Validação

#### Descrição
Adicione operações de criação, atualização e remoção de tarefas, usando modelos Pydantic para validar o payload e retornando erros HTTP apropriados.

#### Requisitos
O programa concluído deve:

- Criar o endpoint `POST /tasks` para adicionar uma nova tarefa com `title` obrigatório.
- Criar o endpoint `PUT /tasks/{task_id}` para atualizar `title` e `done`.
- Criar o endpoint `DELETE /tasks/{task_id}` para remover uma tarefa existente.
- Retornar `404 Not Found` quando o `task_id` não existir.
- Garantir validação de entrada com modelos Pydantic.
