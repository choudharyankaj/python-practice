from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Data model
class User(BaseModel):
    name: str
    email: str
    age: int

# Fake database
users = []

# CREATE
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created", "user": user}

# READ all
@app.get("/users")
def get_users():
    return users

# READ single
@app.get("/users/{index}")
def get_user(index: int):
    if index >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    return users[index]

# UPDATE
@app.put("/users/{index}")
def update_user(index: int, user: User):
    if index >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    users[index] = user
    return {"message": "User updated", "user": user}

# DELETE
@app.delete("/users/{index}")
def delete_user(index: int):
    if index >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users.pop(index)
    return {"message": "User deleted", "user": deleted_user}
