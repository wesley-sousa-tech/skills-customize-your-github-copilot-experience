"""Starter code: Building REST APIs with FastAPI.

Execute localmente:
    pip install fastapi uvicorn
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Tasks API")

# Banco em memoria para simplificar a atividade.
TASKS = []
NEXT_ID = 1


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    done: bool | None = None


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    return TASKS


@app.post("/tasks", status_code=201)
def create_task(payload: TaskCreate):
    global NEXT_ID

    new_task = {
        "id": NEXT_ID,
        "title": payload.title,
        "done": False,
    }
    TASKS.append(new_task)
    NEXT_ID += 1
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, payload: TaskUpdate):
    for task in TASKS:
        if task["id"] == task_id:
            if payload.title is not None:
                task["title"] = payload.title
            if payload.done is not None:
                task["done"] = payload.done
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(TASKS):
        if task["id"] == task_id:
            TASKS.pop(index)
            return None

    raise HTTPException(status_code=404, detail="Task not found")
