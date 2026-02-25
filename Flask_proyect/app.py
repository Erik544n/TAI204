from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_URL = "http://localhost:5000/v1/usuarios/"

@app.route('/')
def index():
    usuarios_lista = [] 
    
    try:
        respuesta = requests.get(API_URL)
        
        if respuesta.status_code == 200:
            datos_api = respuesta.json()
            usuarios_lista = datos_api.get("Usuarios", [])
        else:
            print(f"La API respondió con error: {respuesta.status_code}")
            
    except Exception as e:
        print(f"DEBUG: Error de conexión real: {e}")

    return render_template('index.html', usuarios=usuarios_lista)


@app.route('/agregar', methods=['POST'])
def agregar_usuario():
    nuevo_usuario = {
        "id": int(request.form.get('id')),
        "nombre": (request.form.get('nombre')),
        "edad": int(request.form.get('edad'))
    }

    try:
        requests.post(API_URL, json=nuevo_usuario)
    except:
        print(f"Error al crear nuevo usuario: {e}")
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    try:
        url_eliminar = f"{API_URL}{id}" 
        
        respuesta = requests.delete(url_eliminar)
        
        if respuesta.status_code == 200:
            print(f"Usuario {id} eliminado con éxito.")
        else:
            print(f"Error al eliminar: {respuesta.status_code}")
            
    except Exception as e:
        print(f"Error de conexión al eliminar: {e}")
        
    return redirect(url_for('index'))
    


if __name__ == '__main__':
    app.run(debug=True, port=5020)