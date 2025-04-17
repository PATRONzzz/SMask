from asyncio import Task

from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from db.repository.task import create_new_task
from db.session import get_db
from schemas.task import TaskCreate

router = APIRouter()


@router.post(
    "/task",
    status_code=status.HTTP_201_CREATED,
)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    task = create_new_task(task=task, db=db)
    return task
