from fastapi import status, HTTPException, Depends, APIRouter
from app.data.database import usuarios
from app.models.usuarios import crear_Usuario
from app.security.aut import verificar_peticion

router = APIRouter(
    prefix="/v1/usuarios", tags=['CRUD HTTP']
)


## Nuevo endPoint
@router.get("/")
async def consultaT():
    return{
        "status":"200",
        "total":len(usuarios),
        "Usuarios":usuarios
    }

##
@router.post("/")
async def agregar_usuario(usuario:crear_Usuario): 
    for usr in usuarios:
        if usr["id"] == usuario.id:
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

@router.put("/{id}")
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

@router.delete("/{id}")
async def eliminar_usuario(id:int, usuarioAut:str=Depends(verificar_peticion)):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)

            return{
                "mesaje":f"Usuario eliminado por {usuarioAut}",
                "usuario":usr,
                "status":200
            }
