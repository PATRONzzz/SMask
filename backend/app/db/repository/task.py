from sqlalchemy.orm import Session

from db.models.task import Task
from schemas.task import TaskCreate


# создание задачи
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


# возвращение задачи
def retreive_task(id: int, db: Session):
    task = db.query(Task).filter(Task.id == id).first()
    return task
