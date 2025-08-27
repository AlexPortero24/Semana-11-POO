# inventario.py
# Clase que gestiona el inventario completo, ahora con persistencia en archivo y manejo de excepciones

import os  # Para verificar si existe el archivo
from producto import Producto  # Importamos la clase Producto para poder usarla aquí

class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa la lista de productos y carga los productos existentes desde el archivo 'inventario.txt'.
        """
        self.productos = []        # Lista que almacenará objetos Producto
        self.archivo = "inventario.txt"  # Nombre del archivo donde se guardará el inventario
        self.cargar_archivo()  # Llamamos al método para cargar productos desde el archivo al iniciar
        self.productos_dict={} # AÑADIDO semana 11 Diccionario para acceso rapido por id_producto
        #sincronizacion diccionario con la lista inicial
        for p in self.productos:
            self.productos_dict[p.get_id()]= p

    def guardar_archivo(self):
        """
        Guarda todos los productos actuales en el archivo 'inventario.txt'.
        Se sobrescribe todo el archivo para reflejar el estado actual del inventario.
        """
        try:
            with open(self.archivo, "w") as f:  # Abrimos el archivo en modo escritura ('w')
                for p in self.productos:
                    # Escribimos cada producto en una línea con formato: id,nombre,cantidad,precio
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
        except PermissionError:
            # Si no se puede escribir en el archivo (falta de permisos), se muestra un mensaje
            print("Error: No se puede escribir en el archivo de inventario.")

    def cargar_archivo(self):
        """
        Carga los productos existentes desde 'inventario.txt' al iniciar el inventario.
        Si el archivo no existe, se crea vacío.
        """
        if not os.path.exists(self.archivo):
            # Si el archivo no existe, lo creamos vacío
            open(self.archivo, "w").close()
            return  # Salimos, no hay productos que cargar
        try:
            with open(self.archivo, "r") as f:  # Abrimos el archivo en modo lectura ('r')
                for linea in f:
                    linea = linea.strip()  # Quitamos espacios o saltos de línea al inicio y final
                    if linea:  # Evitamos procesar líneas vacías
                        # Separamos los datos usando la coma como separador
                        id_producto, nombre, cantidad, precio = linea.split(",")
                        # Creamos un objeto Producto con los datos del archivo
                        producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                        # Agregamos el producto a la lista de productos
                        self.productos.append(producto)
        except (FileNotFoundError, PermissionError) as e:
            # Capturamos errores de archivo y notificamos al usuario
            print(f"Error al cargar el archivo: {e}")

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario si su ID es único.
        Luego guarda automáticamente los cambios en el archivo.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)  # Agregamos el producto a la lista
        print("Producto agregado correctamente.")
        self.guardar_archivo()  # Guardamos los cambios en el archivo

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.
        Luego guarda automáticamente los cambios en el archivo.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)  # Eliminamos el producto de la lista
                print("Producto eliminado correctamente.")
                self.guardar_archivo()  # Guardamos los cambios
                return
        print("Error: Producto no encontrado.")  # Mensaje si no existe el ID

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o precio de un producto por su ID.
        Si no se pasa un valor, no se modifica ese atributo.
        Luego guarda automáticamente los cambios en el archivo.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)  # Actualizamos la cantidad
                if precio is not None:
                    p.set_precio(precio)      # Actualizamos el precio
                print("Producto actualizado correctamente.")
                self.guardar_archivo()      # Guardamos cambios en el archivo
                return
        print("Error: Producto no encontrado.")  # Si no existe el ID

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre (puede ser parcial).
        Devuelve una lista con todos los productos que coincidan.
        """
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        """
        Muestra todos los productos del inventario.
        Si no hay productos, avisa que el inventario está vacío.
        """
        if not self.productos:
            print("El inventario está vacío.")
            return
        for p in self.productos:
            print(p)  # Imprime cada producto usando su método __str__ de la clase Producto

# Métodos nuevos usando diccionario
    def obtener_producto_por_id(self, id_producto):
        """
        Devuelve el producto directamente usando el diccionario para acceso rápido por ID.
        """
        return self.productos_dict.get(id_producto, None)

    def mostrar_todos_los_productos_diccionario(self):
        """
        Muestra todos los productos usando el diccionario.
        Útil si se quiere iterar directamente sobre el diccionario.
        """
        if not self.productos_dict:
            print("El inventario está vacío.")
            return
        for id_p, producto in self.productos_dict.items():
            print(producto)
