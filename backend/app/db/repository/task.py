from sqlalchemy.orm import Session

from db.models.task import Task
from schemas.task import TaskCreate


# Создание задачи
def create_new_task(task: TaskCreate, db: Session, owner_id: int = 1):
    task = Task(
        title=task.title,
        task=task.task,
        description=task.description,
        owner_id=owner_id,
        slug=task.slug,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


# Возвращение задачи
def retreive_task(id: int, db: Session):
    task = db.query(Task).filter(Task.id == id).first()
    return task


# Получение списка задач, для пользователя
def get_all_tasks(db: Session, owner_id: int = None):
    tasks = db.query(Task)
    if owner_id:
        tasks = tasks.filter(Task.owner_id == owner_id)
    tasks = tasks.all()
    return tasks


# Получение задач по статусу
def get_tasks_by_status(status: str, db: Session):
    tasks = db.query(Task).filter(Task.status == status).all()
    return tasks
