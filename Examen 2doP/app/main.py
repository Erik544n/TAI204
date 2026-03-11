from fastapi import FastAPI
from typing import Optional, literal
from pydantic import BaseModel, field, field_validator




usuarios = [
    {"id":1, "nombre":"Erik", }


]



tramite = [
    {"id":1, "tramite":"deposito"},
    {"id":2, "tramite":"retiro"},
    {"id":3, "tramite":"consulta"},

]

Turnos = []


class usuario (basemodel):
    id: int = Field(...,gt=0)
    nombre: str = Field(...,min_legth=2)


class crear_Turnos (baseModel):
    usuario_id: int = field(...,gt=)


@app.post("/v1/turnos/", tags=['CRUD HTTP'])
async def crear_turnos():




@app.get("/v1/turnos", tags=['CRUD HTTP'])
async def listar_turnos():
    
    return{
        "status":200
        
    }


@app.get("/v1/turnos{id_turnos}", tags=['CRUD HTTP'])
async def listar_turnos_id(usuarios:id):












