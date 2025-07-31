from pymongo import MongoClient
from app.models.user import UserInDB
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "usuarios_db")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]
usuarios_collection = db["usuarios"]

def guardar_usuario(user: UserInDB):
    usuario_dict = user.dict()
    usuario_dict["_id"] = str(user.id)
    usuarios_collection.insert_one(usuario_dict)
    return user

def correo_ya_existe(email: str):
    return usuarios_collection.find_one({"email": email}) is not None
