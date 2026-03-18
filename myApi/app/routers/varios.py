from typing import Optional
import asyncio
from app.data.database import usuarios
from fastapi import APIRouter

routerV = APIRouter(
    tags=['Inicio']

)

# endPoints
@routerV.get("/holaMundo" )
async def hola():
    await asyncio.sleep(5)         #peticioón, consultaBD, Archivo 
    return {
        "mensaje":"Hola Mundo",
        "status":200
        }
@routerV.get("/v1/ParametroOb/{id}")
async def consultaUno(id:int):
    return{"mensaje":"Usuario Encontrado",
        "usuario":id,
        "status":"200"
    }

@routerV.get("/v1/ParametroOp/")
async def consultaTodos(id:Optional[int]= None):

    if id is not None:
        for usuarioK in usuarios:
            if usuarioK["id"] == id:
                return{"mensaje":"Usuario Encontrado","usuario":usuarioK,
                "Status":"200"
                }
        return{"mensaje":"Usuario no encontrado", 
            "status":"200"
        }

    else:
        return{"mensaje":"No se proporciono un Id",
        "status":"200"
        }

