from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

################
# SEGURIDAD CON HTTP BASIC  
################

security = HTTPBasic()

def verificar_peticion(credenciales:HTTPBasicCredentials=Depends(security)):
    usuarioAut= secrets.compare_digest(credenciales.username, "Erik")
    contraAut = secrets.compare_digest(credenciales.password, "12345")

    if not (usuarioAut and contraAut):
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail = "Credenciales no Autorizadas"

        )
    return credenciales.username 
