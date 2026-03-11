from fastapi import FastAPI
from typing import Optional, literal
from pydantic import BaseModel, field, field_validator




usuarios = [
    {"id":1, "nombre":"Erik"}

]


TRAMINES = [
    {"id":1, "tramite":"deposito"},
    {"id":2, "tramite":"retiro"},
    {"id":3, "tramite":"consulta"},

]

Turnos = []


class usuario (basemodel):
    id: int = Field(...,gt=0)
    nombre: str = Field(...,min_legth=8)


class crear_Turnos (baseModel):
    usuarios_id: int
    TRAMINES_id: int 
    


@app.post("/v1/turnos/", tags=['CRUD HTTP'])
async def crear_turnos(datos):

    usuario = next ((u for u in usuarios 
    if u ["id"] == datos.usuario_id), None)

    tramite = next ((i for i in tramine 
    if i ["id"] == datos.TRAMINES_id), None)


    if not usuario or not tramite:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Usuario o tramite no encontrado"
        )

    nuevo_tur = {
        "TRAMITE_id": len(Turnos) + 1,
        "usuarios_id": usuario["nombre"],
        
    }

    return {"mensaje":"Turno registrado con éxito"}



@app.get("/v1/turnos", tags=['CRUD HTTP'])
async def listar_turnos():
    return{
        "status":200
        
    }


@app.get("/v1/turnos/{id_turnos}", tags=['CRUD HTTP'])
async def listar_turnos(id_turnos:id):

    return{
        "status":200
    }


@app.delete("/v1/turnos/{id_turno}", tags=['CRUD HTTP'])
async def eliminar_turno(id_turno:id):

    if turno is None:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail="El turno ya no existe"
        )
    
    return {"mensaje":"Se Elimino el turno"}



@app.put ("/v1/turnos_Antendidos/", tags=['CRUD HTTP'])
async def Marcar_turnos_atendidos(turnos:id):


    return{"mesaje":"Turno marcado como atendido"}






