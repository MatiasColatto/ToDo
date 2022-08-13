from starlette.requests import Request
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.users import user
from routes.tasks import task
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:8080/users",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes
app.include_router(user)
app.include_router(task, prefix='/tasks')

# General Methods
@app.get('/')
def root():
    # Validate if the users and passwords are correct
    return {'message': 'Hello World'}
