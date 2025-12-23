from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from projects.crud.student_system.database import get_db
import projects.crud.student_system.models as models
import projects.crud.student_system.schemas as schemas

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# Create Student
# @router.post("/", response_model=schemas.StudentResponseSchema)
# def create_student(student: schemas.StudentCreateSchema, db: Session = Depends(get_db)):
#     new_student = models.Student(name=student.name, age=student.age, group=student.group)
#     db.add(new_student)
#     db.commit()
#     db.refresh(new_student)
#     return new_student

@router.post("/", response_model=schemas.StudentResponseSchema)
async def create_student(student: schemas.StudentCreateSchema, db: Session = Depends(get_db)):
    new_student = models.Student(name=student.name, age=student.age, group=student.group)
    db.add(new_student)
    db.commint()
    db.refresh()
    return new_student


# Get All Students
@router.get("/", response_model=list[schemas.StudentResponseSchema])
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

# Get One Student
@router.get("/{student_id}", response_model=schemas.StudentResponseSchema)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update Student
@router.put("/{student_id}", response_model=schemas.StudentResponseSchema)
def update_student(student_id: int, data: schemas.StudentCreateSchema, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.name = data.name
    student.age = data.age
    db.commit()
    db.refresh(student)
    return student

# Delete Student
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    # student = db.query(models.Student).filter(models.Student.id == student_id).first()
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}