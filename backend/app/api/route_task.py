from asyncio import Task

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from db.repository.task import create_new_task, retreive_task
from db.session import get_db
from schemas.task import ShowTask, TaskCreate

router = APIRouter()


@router.post(
    "/tasks",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowTask,
)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    task = create_new_task(task=task, db=db)
    return task


@router.get("/tasks/{id}", response_model=ShowTask)
def get_task(id: int, db: Session = Depends(get_db)):
    task = retreive_task(id=id, db=db)
    if not task:
        raise HTTPException(
            detail=f"Task with ID {id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return task
