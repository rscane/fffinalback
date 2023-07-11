import sqlite3
from flask import Flask,  jsonify, request
from flask_cors import CORS
from levantar_db import get_db_connection


class Producto:
    
    def __init__(self, id, precio, title, cantidad, ):
        self.id = id           
        self.precio = precio 
        self.title = title
        self.cantidad = cantidad                 

    def modificar(self, nuevo_precio, nueva_cantidad):
        self.precio = nuevo_precio 
        self.cantidad = nueva_cantidad        
        

class Inventario:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()

    def agregar_producto(self, id, precio, title, cantidad):
        producto_existente = self.consultar_producto(id)
        if producto_existente:
            return jsonify({'message': 'Ya existe un producto con ese id.'}), 400
        self.cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (id, precio, title, cantidad))
        self.conexion.commit()
        return jsonify({'message': 'se agregó el producto exitosamente.'}), 200

    def consultar_producto(self, id):
        self.cursor.execute("SELECT * FROM productos WHERE codigo = ?", (id,))
        row = self.cursor.fetchone()
        if row:
            id, precio, title, cantidad = row
            return Producto(id, precio, title, cantidad)
        return None

    def modificar_producto(self, id, nuevo_precio, nueva_cantidad):
        producto = self.consultar_producto(id)
        if producto:
            self.cursor.execute("UPDATE productos SET precio = ?, cantidad = ? WHERE id = ?", (nuevo_precio, nueva_cantidad, id))
            self.conexion.commit ()
            return jsonify({'message': 'Producto modificado correctamente.'}), 200
        return jsonify({'message': 'Producto no encontrado.'}), 404

    def eliminar_producto(self, id):
        self.cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        if self.cursor.rowcount > 0:
            self.conexion.commit()
            return jsonify({'message': 'Producto eliminado correctamente.'}), 200
        return jsonify({'message': 'Producto no encontrado.'}), 404
    
    def mostrar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()
        productos = []
        for row in rows:
            id, precio, title, cantidad = row
            producto = {'id': id, 'precio': precio, 'nombre': title, 'cantidad': cantidad}
            productos.append(producto)
        return jsonify(productos), 200

app = Flask(__name__)
CORS(app)

inventario = Inventario()
@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = inventario.consultar_producto(id)
    if producto:
        return jsonify({
            'id': producto.id,
            'precio': producto.precio,
            'title': producto.title,
            'cantidad': producto.cantidad
        }), 200
    return jsonify({'message': 'Producto no encontrado.'}), 404
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return inventario.mostrar_productos()
@app.route('/productos', methods=['POST'])
def agregar_producto():
    id = request.json.get('id')
    precio = request.json.get('precio')
    title = request.json.get('title')
    cantidad = request.json.get('cantidad')
    return inventario.agregar_producto(id, precio, title, cantidad)
@app.route('/productos', methods=['PUT'])
def modificar_producto():
    id = request.json.get('id')
    nuevo_precio = request.json.get('precio')
    nueva_cantidad = request.json.get('cantidad')
    return inventario.modificar_producto(id, nuevo_precio, nueva_cantidad)
@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    return inventario.eliminar_producto(id)


if __name__ == '__main__':
    app.run()

