/* *Acción para que aparezca y desaparezca la lista en movil */
const button = document.querySelector('.button')
const nav = document.querySelector('.nav')

button.addEventListener('click',()=>{
    nav.classList.toggle('activo')
})

// validacion formulario
function validarFormulario() {
    let nombre = document.getElementById("nombre").value.trim();
    let email = document.getElementById("email").value.trim();
    let mensaje = document.getElementById("mensaje").value.trim();

    if ((nombre === "" || email === "" || mensaje === "")) {
        alert("No te olvides de llenar todos los campos del formulario");
        return false
    }

    for (let i = 0; i < nombre.length; i++) {
        let letrasEnNombre = nombre.charCodeAt(i);
        if (!((letrasEnNombre >= 65 && letrasEnNombre <= 90) || (letrasEnNombre >= 97 && letrasEnNombre <= 122) || letrasEnNombre === 32)) {
            alert("El campo nombre solo acepta letras mayúsculas y minúsculas, no tildes ni caracteres especiales ");
            return false;
        }
    }

alert("Tu mensaje fue enviado correctamente!");
return true;
}

const URL = "rsanchezc.pythonanywhere.com"
// Alta de producto-
document.getElementById('formInv').addEventListener('submit', function (event) {
    event.preventDefault(); 
    var id = document.getElementById('iditem').value;
    var precio = document.getElementById('precio').value;
    var title = document.getElementById('title').value;
    var cantidad = document.getElementById('cantidad').value;

    var producto = {
    id: id,
    precio: precio,
    title: title,
    cantidad: cantidad
    };

    fetch(URL + 'productos', {
    method: 'POST',
    headers: {
    'Content-Type': 'application/json'
    },
    body: JSON.stringify(producto)
    })
    .then(function (response) {
    if (response.ok) {
    return response.json(); 
    } else {
    throw new Error('No se pudo agregar el producto.');
    }
    })
    .then(function (data) {
    alert('Producto agregado correctamente.');
    document.getElementById('iditem').value = "";
    document.getElementById('precio').value = "";
    document.getElementById('title').value = "";
    document.getElementById('cantidad').value = "";
    })
    .catch(function (error) {
    alert('no se pudo agregar el producto');
    });
    })

    // inventario
fetch(URL + 'productos/')
.then(function (response) {
if (response.ok) {
return response.json(); 
} else {
throw new Error('Error al obtener los productos.');
}
})
.then(function (data) {
var tablaProductos = document.getElementById('tablaProductos');
data.forEach(function (producto) {
var fila = document.createElement('tr');
fila.innerHTML = '<td>' + producto.id + '</td>' +
'<td>' + producto.precio + '</td>' +
'<td align="right">' + producto.title + '</td>' +
'<td align="right">&nbsp; &nbsp;&nbsp; &nbsp;' + producto.cantidad + '</td>';
tablaProductos.appendChild(fila);
});
})
.catch(function (error) {
alert('Error al obtener los productos.');
});
//editar prod
