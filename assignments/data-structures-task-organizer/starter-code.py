"""Starter code: Smart Task Organizer.

Objetivo: praticar listas, dicionarios e conjuntos com foco em consultas e ordenacao.
"""


def build_task_index(tasks):
    """Retorna um dicionario mapeando id -> tarefa."""
    return {task["id"]: task for task in tasks}


def filter_by_status(tasks, status):
    """Filtra tarefas por status."""
    return [task for task in tasks if task["status"] == status]


def unique_tags(tasks):
    """Retorna o conjunto de tags unicas."""
    tags = set()
    for task in tasks:
        tags.update(task["tags"])
    return tags


def sort_by_priority(tasks):
    """Ordena tarefas por prioridade (maior para menor)."""
    return sorted(tasks, key=lambda task: task["priority"], reverse=True)


def count_by_status(tasks):
    """Conta quantas tarefas existem por status."""
    counts = {}
    for task in tasks:
        status = task["status"]
        counts[status] = counts.get(status, 0) + 1
    return counts


def sample_tasks():
    """Dados iniciais para comecar a atividade."""
    return [
        {"id": 1, "title": "Revisar variaveis", "priority": 2, "status": "done", "tags": ["python", "basics"]},
        {"id": 2, "title": "Resolver lista de loops", "priority": 4, "status": "doing", "tags": ["python", "loops"]},
        {"id": 3, "title": "Ler sobre classes", "priority": 3, "status": "todo", "tags": ["oop", "python"]},
        {"id": 4, "title": "Praticar dicionarios", "priority": 5, "status": "todo", "tags": ["python", "dict"]},
        {"id": 5, "title": "Corrigir exercicios", "priority": 1, "status": "doing", "tags": ["practice"]},
        {"id": 6, "title": "Assistir aula gravada", "priority": 2, "status": "done", "tags": ["review"]},
        {"id": 7, "title": "Refatorar codigo", "priority": 4, "status": "todo", "tags": ["quality", "python"]},
        {"id": 8, "title": "Montar resumo", "priority": 3, "status": "doing", "tags": ["study"]},
    ]


def main():
    tasks = sample_tasks()

    print("Total de tarefas:", len(tasks))

    index = build_task_index(tasks)
    print("Acesso rapido por id (id=4):", index.get(4))

    todo_tasks = filter_by_status(tasks, "todo")
    print("Tarefas com status 'todo':", len(todo_tasks))

    tags = unique_tags(tasks)
    print("Tags unicas:", sorted(tags))

    sorted_tasks = sort_by_priority(tasks)
    print("Top 3 prioridades:")
    for task in sorted_tasks[:3]:
        print(f"- {task['title']} (prioridade {task['priority']})")

    print("Resumo por status:", count_by_status(tasks))


if __name__ == "__main__":
    main()
