# importaciones
from fastapi import FastAPI 
from typing import Optional
import asyncio

# Instancia del servidor
app = FastAPI(
    title="Mi primer API",
    description="Erik Narciso Bernardino",
    version="1.0"

)


usuarios = [
    {"id":1, "nombre":"Diego", "edad":21},
    {"id":2, "nombre":"Coral", "edad":21},
    {"id":3, "nombre":"Saúl", "edad":21},
]



# endPoints
@app.get("/", tags=['Inicio'])
async def bienvenido():
     #{"aqui va la Clave / index":"aqui va el Valor de la clave"}
    return {"mensaje":"Bienvenido FasAPI"}


# endPoints
@app.get("/holaMundo", tags=['Asincronia'])
async def hola():
    await asyncio.sleep(5)         #peticioón, consultaBD, Archivo 
    return {
        "mensaje":"Hola Mundo",
        "status":200
        }

@app.get("/v1/usuario/{id}", tags=['Parametro Obligatorio'])
async def consultaUno(id:int):

    return{"mensaje":"Usuario Encontrado",
        "usuario":id,
        "status":"200"
    }

@app.get("/v1/usuarios/", tags=['Parametro Opcional'])
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



    