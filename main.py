from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    email: str

@app.get("/")
def home():
    return {"message": "User Microservice Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {
        "message": "User created",
        "user": user
    }

@app.get("/users")
def get_users():
    return users