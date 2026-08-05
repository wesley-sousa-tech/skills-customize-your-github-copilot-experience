# 📘 Assignment: Smart Task Organizer

## 🎯 Objective

Aplicar listas, dicionarios e conjuntos para modelar, consultar e organizar tarefas com foco em eficiencia e clareza de codigo.

## 📝 Tasks

### 🛠️ Build the Task Registry

#### Descrição
Implemente uma estrutura inicial para armazenar tarefas usando uma lista de dicionarios. Cada tarefa deve conter: `id`, `title`, `priority`, `status` e `tags`.

#### Requisitos
O programa completo deve:

- Criar uma lista com pelo menos 8 tarefas de exemplo
- Garantir que cada tarefa use os 5 campos obrigatorios
- Exibir a quantidade total de tarefas cadastradas


### 🛠️ Implement Fast Queries

#### Descrição
Crie funcoes para consultar tarefas por status e por tag. Use dicionarios para facilitar acesso por `id` e conjuntos para remover repeticoes quando necessario.

#### Requisitos
O programa completo deve:

- Implementar `build_task_index(tasks)` retornando um dicionario `{id: task}`
- Implementar `filter_by_status(tasks, status)` retornando apenas tarefas do status informado
- Implementar `unique_tags(tasks)` retornando um conjunto com todas as tags sem duplicatas


### 🛠️ Sort and Report Results

#### Descrição
Implemente ordenacao por prioridade e gere um pequeno relatorio final que ajude a avaliar produtividade.

#### Requisitos
O programa completo deve:

- Ordenar tarefas por `priority` (maior para menor)
- Exibir total de tarefas por status (ex.: `todo`, `doing`, `done`)
- Mostrar as 3 tarefas de maior prioridade em um resumo final
