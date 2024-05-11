from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Starter",
    description="FastAPI Starter Template",
    version="0.1.0",
    docs_url="/docs",
    redoc_url=None,
)


class User(BaseModel):
    name: str
    age: int
    email: str
    password: str
    address: Optional[str] = None


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/users/{user_id}")
def read_item(user_id: int, q: str = None):
    return {"id": user_id, "q": q}


@app.post("/users/")
def create_user(user: User):
    user_dict = user.dict()
    if not user.address:
        user_dict.update({"address": ""})

    return {"id": 1, **user_dict}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"id": user_id, **user.dict()}
