from fastapi import FastAPI, HTTPException
from typing import List
from datetime import datetime
from models import UserCreate, UserRead, TaskCreate, TaskRead, TaskStatus

app = FastAPI()

# In-memory stores
users_db = {}
tasks_db = {}

@app.get("/")
def root():
    return {"message": "🎯 Welcome to the Enhanced Task Tracker API!"}

# Create a user
@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    user_data = user.dict()
    user_data["id"] = user_id
    users_db[user_id] = user_data
    return user_data

# Get all users
@app.get("/users/", response_model=List[UserRead])
def get_users():
    return list(users_db.values())

# Create a task
@app.post("/tasks/", response_model=TaskRead)
def create_task(task: TaskCreate):
    if task.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    task_id = len(tasks_db) + 1
    now = datetime.utcnow()
    task_data = task.dict()
    task_data.update({
        "id": task_id,
        "created_at": now,
        "updated_at": now,
    })
    tasks_db[task_id] = task_data
    return task_data

# Get a single task
@app.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update task status
@app.put("/tasks/{task_id}/status", response_model=TaskRead)
def update_status(task_id: int, status: TaskStatus):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task["status"] = status
    task["updated_at"] = datetime.utcnow()
    return task

# Get all tasks for a user
@app.get("/users/{user_id}/tasks", response_model=List[TaskRead])
def get_user_tasks(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    user_tasks = [task for task in tasks_db.values() if task["user_id"] == user_id]
    return user_tasks