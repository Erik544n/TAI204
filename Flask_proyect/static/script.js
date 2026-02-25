
function agregarUsuario() {
    const idInput = document.getElementById('id');
    const nombreInput = document.getElementById('nombre');
    const edadInput = document.getElementById('edad');

    const datos = {
        id: parseInt(idInput.value),
        nombre: nombreInput.value,
        edad: parseInt(edadInput.value)
    };

    fetch('/api/usuarios', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos)
    })
    .then(response => {
        if (response.ok) {
            const tabla = document.getElementById('tabla-usuarios');
            const nuevaFila = `
                <tr id="fila-${datos.id}">
                    <td>${datos.id}</td>
                    <td>${datos.nombre}</td>
                    <td>${datos.edad}</td>
                    <td>
                        <button onclick="eliminarUsuario('${datos.id}')">Eliminar</button>
                    </td>
                </tr>`;
            tabla.innerHTML += nuevaFila;
            
            idInput.value = '';
            nombreInput.value = '';
            edadInput.value = '';
        } else {
            alert("Error al guardar en la API");
        }
    })
    .catch(error => console.error('Error:', error));
}

// FUNCIÓN PARA ELIMINAR
function eliminarUsuario(id) {
    if (confirm('¿Seguro que deseas eliminar este usuario?')) {
        fetch(`/api/usuarios/${id}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                const fila = document.getElementById(`fila-${id}`);
                if (fila) fila.remove();
            } else {
                alert("Error al eliminar");
            }
        })
        .catch(error => console.error('Error:', error));
    }
}