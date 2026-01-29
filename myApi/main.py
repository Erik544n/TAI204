# importaciones
from fastapi import FastAPI 

import asyncio

# Instancia del servidor
app = FastAPI()

# endPoints
@app.get("/")
async def bienvenido():
     #{"aqui va la Clave / index":"aqui va el Valor de la clave"}
    return {"mensaje":"Bienvenido FasAPI"}


# endPoints
@app.get("/holaMundo")
async def hola():
    await asyncio.sleep(5)         #peticioón, consultaBD, Archivo 
    return {
        "mensaje":"Hola Mundo",
        "status":200
        
        }
