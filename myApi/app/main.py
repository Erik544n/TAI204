# importaciones
from fastapi import FastAPI, status, HTTPException
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

@app.get("/v1/ParametroOb/{id}", tags=['Parametro Obligatorio'])
async def consultaUno(id:int):

    return{"mensaje":"Usuario Encontrado",
        "usuario":id,
        "status":"200"
    }

@app.get("/v1/ParametroOp/", tags=['Parametro Opcional'])
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


## Nuevo endPoint
@app.get("/v1/usuarios/", tags=['CRUD HTTP'])
async def consultaT():

    return{
        "status":"200",
        "total":len(usuarios),
        "Usuarios":usuarios
    }

##
@app.post("/v1/usuarios/", tags=['CRUD HTTP'])
async def agregar_usuario(usuario:dict): 
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(
                status_code= 400,
                detail='El id ya existe'
            )
    usuarios.append(usuario)
    return{
        "Mensaje":"Usuario Agregado",
        "Usuarios":usuario,
        "Status":"200"
    }

@app.put("/v1/usuarios/{id}", tags=['CRUD HTTP'])
async def actualizar_usuario(id:int, usuario_actualizado:dict):
    for usr in usuarios:
        if usr["id"] == id:
            usr["nombre"] = usuario_actualizado.get("nombre", usr["nombre"])
            usr["edad"] = usuario_actualizado.get("edad", usr["edad"])


            return{
                "mensaje":"Usuario actualizado",
                "usuario":usr,
                "status":200
            }


@app.delete("/v1/usuarios/{id}", tags=['CRUD HTTP'])
async def eliminar_usuario(id:int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)

            return{
                "mesaje":"Usuario eliminado",
                "usuario":usr,
                "status":200

            }

