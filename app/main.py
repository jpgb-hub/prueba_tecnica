from fastapi import FastAPI
from app.routes import user_routes

app = FastAPI()

app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"mensaje": "API de usuarios funcionando"}
