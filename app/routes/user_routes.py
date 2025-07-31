from fastapi import APIRouter, HTTPException, status
from app.models.user import UserCreate, UserInDB
from uuid import uuid4
from datetime import datetime
import secrets
from app.db.mongo import guardar_usuario, correo_ya_existe

router = APIRouter()

@router.post("/usuarios", response_model=UserInDB)
def crear_usuario(user: UserCreate):
    if correo_ya_existe(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo ya está registrado"
        )

    now = datetime.utcnow()
    token = secrets.token_hex(16)

    usuario_guardado = UserInDB(
        **user.dict(),
        id=uuid4(),
        created=now,
        modified=now,
        last_login=now,
        token=token,
        isactive=True
    )

    guardar_usuario(usuario_guardado)

    return usuario_guardado
