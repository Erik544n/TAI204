from fastapi import FastAPI, status, HTTPException
from typing import Optional, Literal
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

#################
# Tabla Ficticia
#################

libros = [
    {"id": 1, "Autor": "john katzenbach", "nombre": "La historia del loco", "año": 2004, "Paginas": 504, "estado": "disponible"},
    {"id": 2, "Autor": "john katzenbach", "nombre": "El psicoanalista", "año": 2002, "Paginas": 528, "estado": "disponible"},
    {"id": 3, "Autor": "john katzenbach", "nombre": "Personas Desconocidas", "año": 2016, "Paginas": 464, "estado": "disponible"},
] 

usuarios = [
    {"id": 1, "nombre": "Juanito", "edad": 21, "correo": "juanito@gmail.com"},
    {"id": 2, "nombre": "Erik", "edad": 21, "correo": "narciso@gmail.com"},
    {"id": 3, "nombre": "David", "edad": 21, "correo": "david@gmail.com"},
]

prestamos = []

#################
# Modelos Pydantic
#################

class Registro_Prestamo(BaseModel):
    usuario_id: int
    libro_id: int

class Crear_usuario(BaseModel):
    id: int = Field(..., gt=0)
    nombre: str = Field(..., min_length=2, max_length=100)
    edad: int = Field(..., gt=0)
    correo: str

    @field_validator('correo')
    @classmethod
    def validar_email(cls, v: str) -> str:
        if "@" not in v or "." not in v:
            raise ValueError('El correo debe tener un formato válido (contener @ y punto)')
        return v.lower()

class Crear_libro(BaseModel):
    id: int = Field(..., gt=0)
    Autor: str = Field(..., min_length=2)
    nombre: str = Field(..., min_length=2, max_length=100)
    año: int = Field(..., gt=1450, le=2026)
    paginas: int = Field(..., gt=1)
    estado: Literal["disponible", "prestado"] = Field(default="disponible")

#  ENDPOINTS LIBROS 

@app.get("/v1/libros/", tags=['Libros'])
async def consultar_Libros():
    return {"status": "200", "total": len(libros), "Libros": libros}

@app.get("/v1/libros_Buscar/", tags=['Libros'])
async def consultar_Libros_Nombre(nombre: str):
    for lib in libros:
        if lib["nombre"].lower() == nombre.lower():
            return {"status": "200", "Libro": lib}
    raise HTTPException(status_code=404, detail="Libro no encontrado")

@app.post("/v1/libros/", tags=['Libros'], status_code=status.HTTP_201_CREATED)
async def agregar_libro(libro: Crear_libro):
    if any(l["id"] == libro.id for l in libros):
        raise HTTPException(status_code=400, detail="El id ya existe")
    
    nuevo_libro = libro.model_dump()
    libros.append(nuevo_libro)
    return {"Mensaje": "Libro Creado", "Libros": libros}

#  ENDPOINTS USUARIOS 

@app.post("/v1/Usuario/", tags=['Usuarios'], status_code=status.HTTP_201_CREATED)
async def agregar_usuario(nuevo_usuario: Crear_usuario):
    if any(u["id"] == nuevo_usuario.id for u in usuarios):
        raise HTTPException(status_code=400, detail="El id de usuario ya existe")
    
    usuarios.append(nuevo_usuario.model_dump())
    return {"mensaje": "Usuario agregado", "usuarios": usuarios}

#  ENDPOINTS PRESTAMOS 

@app.post("/v1/prestamos/", tags=['Prestamos'], status_code=status.HTTP_201_CREATED)
async def registrar_prestamo(datos: Registro_Prestamo):
    usuario = next((u for u in usuarios if u["id"] == datos.usuario_id), None)
    libro = next((l for l in libros if l["id"] == datos.libro_id), None)

    if not usuario or not libro:
        raise HTTPException(status_code=404, detail="Usuario o Libro no encontrado")
    
    # 409 Conflict si el libro ya está prestado
    if libro["estado"] == "prestado":
        raise HTTPException(
            status_code= status.HTTP_409_CONFLICT, 
            detail="El libro ya está prestado"
        )

    libro["estado"] = "prestado"
    
    nuevo_p = {
        "id_prestamo": len(prestamos) + 1, 
        "usuario": usuario["nombre"], 
        "libro": libro["nombre"], 
        "libro_id": libro["id"]
    }
    prestamos.append(nuevo_p)
    return {"mensaje": "Prestamo registrado", "detalle": nuevo_p}

@app.put("/v1/prestamos/devolver/{libro_id}", tags=['Prestamos'], status_code=status.HTTP_200_OK)
async def devolver_libro(libro_id: int):
    libro = next((l for l in libros if l["id"] == libro_id), None)
    if not libro: 
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    libro["estado"] = "disponible"
    return {"mensaje": f"El libro '{libro['nombre']}' ahora está disponible"}

@app.delete("/v1/prestamos/{id_prestamo}", tags=['Prestamos'])
async def eliminar_prestamo(id_prestamo: int):
    global prestamos
    prestamo = next((i for i, p in enumerate(prestamos) if p["id_prestamo"] == id_prestamo), None)
    
    # 409 Conflict si el registro de préstamo ya no existe
    if prestamo is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="El registro de préstamo ya no existe"
        )
    
    prestamos.pop(prestamo)
    return {"mensaje": "Registro de préstamo eliminado"}