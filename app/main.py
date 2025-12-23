from fastapi import FastAPI
from learning_modules.path_parameters import router as model_router
import projects.crud.student_system.models as models
from projects.crud.student_system.database import engine
import projects.crud.student_system.students as students
from learning_modules.background_tasks.order_processing.order_processing_01 import order_router


app = FastAPI()

'''
    Learning Modules
'''
app.include_router(model_router)

'''
    Student Management System CRUD API
'''
# Create DB tables
models.Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(students.router)

'''
    Order Processing with Background Task
'''
app.include_router(order_router)

