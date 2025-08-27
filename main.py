# main.py
# Este archivo controla la interacción con el usuario y utiliza las clases Producto e Inventario
# Aquí se maneja todo el menú y se llama a los métodos para agregar, eliminar, actualizar, buscar y mostrar productos

from producto import Producto  # Traemos la clase Producto desde producto.py
from inventario import Inventario  # Traemos la clase Inventario desde inventario.py


def mostrar_menu():
    """
    Función para mostrar el menú de opciones al usuario.
    Cada vez que se ejecuta, el usuario puede elegir qué acción realizar.
    """
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Agregar producto")  # Opción para agregar un nuevo producto
    print("2. Eliminar producto")  # Opción para eliminar un producto existente por ID
    print("3. Actualizar producto")  # Opción para actualizar la cantidad o precio de un producto
    print("4. Buscar producto")  # Opción para buscar productos por nombre
    print("5. Mostrar todos los productos")  # Opción para ver todos los productos del inventario
    print("6. Salir")  # Opción para salir del programa
    print("7. Mostrar producto por ID (usando diccionario)")  # Nueva opción para usar diccionario
    print("8. Mostrar todos los productos (usando diccionario)")  # Iterar sobre diccionario

    opcion= input("seleccione una opcion:") # añadido semana 11
    return opcion

def main():
    """
    Función principal que controla el flujo del programa.
    Aquí se crean las instancias de Inventario y se manejan las opciones del menú.
    """
    inventario = Inventario()  # Creamos una instancia de la clase Inventario

    while True:  # Bucle infinito que mantiene activo el menú hasta que el usuario decida salir
        opcion = mostrar_menu()  # Mostramos el menú y guardamos la opción elegida

        if opcion == "1":  # Si el usuario elige agregar producto
            id_producto = input("Ingrese ID del producto: ")  # Solicitamos el ID del producto
            nombre = input("Ingrese nombre del producto: ")  # Solicitamos el nombre del producto
            try:  # Intentamos convertir las entradas a número
                cantidad = int(input("Ingrese cantidad: "))  # Solicitamos la cantidad y la convertimos a entero
                precio = float(input("Ingrese precio: "))  # Solicitamos el precio y lo convertimos a decimal
            except ValueError:  # Capturamos errores si no se ingresa un número válido
                print("Error: cantidad y precio deben ser números.")  # Mensaje de error
                continue  # Volvemos al inicio del bucle sin agregar el producto
            producto = Producto(id_producto, nombre, cantidad, precio)  # Creamos un objeto Producto
            inventario.agregar_producto(producto)  # Llamamos al método para agregar el producto al inventario

        elif opcion == "2":  # Si el usuario elige eliminar un producto
            id_producto = input("Ingrese ID del producto a eliminar: ")  # Pedimos el ID del producto
            inventario.eliminar_producto(id_producto)  # Llamamos al método para eliminarlo

        elif opcion == "3":  # Si el usuario elige actualizar un producto
            id_producto = input("Ingrese ID del producto a actualizar: ")  # Pedimos el ID
            cantidad = input("Ingrese nueva cantidad (deje vacío si no desea cambiar): ")  # Nueva cantidad opcional
            precio = input("Ingrese nuevo precio (deje vacío si no desea cambiar): ")  # Nuevo precio opcional
            cantidad = int(cantidad) if cantidad.strip() != "" else None  # Convertimos a entero si se ingresó valor
            precio = float(precio) if precio.strip() != "" else None  # Convertimos a decimal si se ingresó valor
            inventario.actualizar_producto(id_producto, cantidad, precio)  # Actualizamos el producto

        elif opcion == "4":  # Si el usuario elige buscar productos
            nombre = input("Ingrese nombre o parte del nombre a buscar: ")  # Pedimos el nombre a buscar
            resultados = inventario.buscar_producto(nombre)  # Buscamos coincidencias en el inventario
            if resultados:  # Si se encontraron productos
                print("Productos encontrados:")  # Mensaje de productos encontrados
                for p in resultados:  # Recorremos la lista de resultados
                    print(p)  # Mostramos cada producto usando __str__ de Producto
            else:  # Si no se encontraron productos
                print("No se encontraron productos con ese nombre.")  # Mensaje de aviso

        elif opcion == "5":  # Si el usuario quiere mostrar todos los productos
            inventario.mostrar_productos()  # Llamamos al método que imprime todos los productos

        elif opcion == "6":  # Si el usuario elige salir
            print("Saliendo del sistema...")  # Mensaje de despedida
            break  # Rompemos el bucle y terminamos el programa
        elif opcion == "7":
            id_producto = input("Ingrese ID del producto a buscar: ")
            producto = inventario.obtener_producto_por_id(id_producto)
            if producto:
                print("Producto encontrado:")
                print(producto)
            else:
                print("No se encontró un producto con ese ID.")

        elif opcion == "8":
            inventario.mostrar_todos_los_productos_diccionario()


        else:  # Si el usuario ingresa una opción inválida
            print("Opción no válida. Intente de nuevo.")  # Mensaje de error


if __name__ == "__main__":
    # Esta condición verifica que el archivo se esté ejecutando directamente
    main()  # Llamamos a la función principal para iniciar el programa