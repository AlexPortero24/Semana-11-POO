# Sistema Avanzado de Gestión de Inventario

## Descripción
Este proyecto implementa un sistema avanzado de gestión de inventarios para una tienda, desarrollado en Python, utilizando Programación Orientada a Objetos (POO) y colecciones para un manejo eficiente de los ítems del inventario. Incluye persistencia en archivos, permitiendo guardar y cargar el inventario automáticamente.

## Archivos del proyecto
- `producto.py` → Clase Producto.  
- `inventario.py` → Clase Inventario con lista y diccionario, métodos CRUD y almacenamiento en archivos.  
- `main.py` → Interfaz de usuario con menú interactivo.  
- `inventario.txt` → Archivo donde se guarda el inventario.  

## 1. Clase Producto
Ubicada en `producto.py`  
- Atributos: `id_producto` (único), `nombre`, `cantidad`, `precio`.  
- Métodos:
  - `get_id()`, `get_nombre()`, `get_cantidad()`, `get_precio()`  
  - `set_id_producto()`, `set_nombre()`, `set_cantidad()`, `set_precio()`  
  - `__str__()`  

## 2. Clase Inventario
Ubicada en `inventario.py`  
- Almacena productos en lista (`self.productos`) y diccionario (`self.productos_dict`).  
- Métodos principales:
  - `agregar_producto(producto)`  
  - `eliminar_producto(id_producto)`  
  - `actualizar_producto(id_producto, cantidad, precio)`  
  - `buscar_producto(nombre)`  
  - `mostrar_productos()`  
  - `obtener_producto_por_id(id_producto)`  
  - `mostrar_todos_los_productos_diccionario()`  

## 3. Integración de colecciones
- Lista (`self.productos`) → operaciones secuenciales (mostrar todos, buscar por nombre).  
- Diccionario (`self.productos_dict`) → acceso rápido a productos por ID, optimizando búsquedas y manejo de datos.  

## 4. Almacenamiento en archivos
- Archivo: `inventario.txt`  
- Métodos:
  - `guardar_archivo()` → guarda productos de la lista en el archivo.  
  - `cargar_archivo()` → carga productos desde el archivo al iniciar el inventario.  

## 5. Interfaz de usuario
Ubicada en `main.py`  
- Menú interactivo con opciones:
  1. Agregar producto  
  2. Eliminar producto  
  3. Actualizar producto  
  4. Buscar producto  
  5. Mostrar todos los productos  
  6. Salir  
  7. Mostrar producto por ID usando diccionario  
  8. Mostrar todos los productos usando diccionario  


## 7. Los datos se guardan automáticamente en `inventario.txt`.  

## Notas importantes
- Se añadió un diccionario (`productos_dict`) para optimizar el acceso rápido a los productos por su ID.  
- Todas las operaciones principales mantienen la sincronización entre la lista y el diccionario.  
- El sistema permite tanto operaciones tradicionales por lista como optimizadas por diccionario.
