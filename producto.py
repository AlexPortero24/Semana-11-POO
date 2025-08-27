# producto.py
# Clase que representa un producto en el inventario

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor de la clase Producto: aquí se definen las características del producto
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre            # Nombre del producto
        self.cantidad = cantidad        # Cantidad disponible
        self.precio = precio            # Precio unitario

    # Getters: funciones para obtener el valor de cada atributo
    def get_id(self):
        return self.id_producto  # Devuelve el ID del producto

    def get_nombre(self):
        return self.nombre      # Devuelve el nombre del producto

    def get_cantidad(self):
        return self.cantidad    # Devuelve la cantidad del producto

    def get_precio(self):
        return self.precio      # Devuelve el precio del producto

    # Setters: funciones para modificar los valores de los atributos
    def set_nombre(self, nombre):
        self.nombre = nombre  # Cambia el nombre del producto

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad  # Cambia la cantidad del producto

    def set_precio(self, precio):
        self.precio = precio  # Cambia el precio del producto

    def set_id_producto(self, id_producto): # Cambiar el id_producto del producto / añadido semana 11
        self.set_id_producto = id_producto

    def __str__(self):
        # Devuelve una cadena con la información del producto, útil para mostrarlo
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
