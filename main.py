from utils.helpers import *
from utils import db_manager 
import sys

def mostrar_tabla (productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    
    print(f"{'ID':<5} {'NOMBRE':<20} {'CATEGORIA':<30} {'PRECIO':<10} {'CANTIDAD':<10}")
    print("-" * 65)
    for prod in productos:
        print (f"{prod[0]:<5} {prod[1]:<20} {prod[5]:<30} {prod[4]:<10.2f} {prod[3]:<10}")
    print("-" * 65)
    
def menu_registrar():
    imprimir_titulo("Registrar Nuevo Producto")
    nombre = validar_input_string("Ingrese el nombre del producto")
    descripcion = input("Ingrese la descripción del producto (opcional): ").strip()
    categoria = validar_input_string("Ingrese la categoría del producto: ")
    cantidad = validar_input_int("Ingrese la cantidad del producto: ")
    precio = validar_input_float("Ingrese el precio del producto: ")
    
    if db_manager.registrar_producto(nombre, descripcion, cantidad, precio, categoria):
        imprimir_exito("Producto registrado exitosamente.")
        
def menu_mostrar():
    imprimir_titulo("Lista de Productos")
    productos = db_manager.obtener_productos()
    mostrar_tabla(productos)

def menu_actualizar():
    imprimir_titulo("Actualizar Producto")
    menu_mostrar()
    product_id = validar_input_int("Ingrese el ID del producto a actualizar: ")
    producto_actual = db_manager.buscar_producto_id(product_id)
    
    if not producto_actual:
        imprimir_error("Producto no encontrado.")
        return
    print(f"Editando: {producto_actual[1]}")
    print("Deja vacio el campo que no quiere modificar")
    
    nuevo_nombre = input(f"Nombre [{producto_actual[1]}]: ").strip() or producto_actual[1]
    nueva_descripcion = input(f"Descripcion [{producto_actual[2]}]: ").strip() or producto_actual[2]
    
    cantidad_str = input(f"Cantidad [{producto_actual[3]}]: ").strip()
    nueva_cantidad = int(cantidad_str) if cantidad_str.isdigit() else producto_actual[3]
    
    precio_str = input(f"Precio [{producto_actual[4]}]: ").strip()
    nuevo_precio = float(precio_str) if precio_str else producto_actual[4]

    nueva_categoria = input(f"Categoria [{producto_actual[5]}]: ").strip() or producto_actual[5]
    
    if db_manager.actualizar_producto(product_id, nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria):
        imprimir_exito("Producto actualizado exitosamente.")
    else :
        imprimir_error("No se realizaron cambios en el producto.")
        
def menu_eliminar():
    imprimir_titulo("Eliminar Producto")
    menu_mostrar() 
    
    id_producto = validar_input_int("Ingrese el ID del producto a eliminar: ")
    confirmacion = input(f"¿Está seguro de que desea eliminar el producto con ID {id_producto}? (s/n): ").strip().lower()
    if confirmacion == 's':
        if db_manager.eliminar_producto(id_producto):
            imprimir_exito("Producto eliminado exitosamente.")
        else:
            imprimir_error("No se encontró el producto.")

def menu_buscar():
    imprimir_titulo("Buscar Producto")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre o Categoría")
    opcion = input ("Opcion: ")
    
    if opcion == '1':
        product_id = validar_input_int("Ingrese el ID del producto a buscar: ")
        res = db_manager.buscar_producto_id(product_id)
        if res:
            mostrar_tabla([res])
        else:
            imprimir_error("Producto no encontrado.")
    elif opcion == '2':
        termino = validar_input_string("Ingrese el término de búsqueda (nombre o categoría): ")
        res = db_manager.buscar_producto_texto(termino)
        if res:
            mostrar_tabla(res)
        else:
            imprimir_error("No se encontraron productos que coincidan con la búsqueda.")

def menu_reporte():
    imprimir_titulo("Reporte de Stock Bajo")
    limite = validar_input_int("Ingrese el límite de cantidad para el reporte: ")
    res = db_manager.reporte_bajo_stock(limite)
    if res:
        imprimir_exito(f"Se encontraron {len(res)} productos con stock bajo {limite}.")
        mostrar_tabla(res)
    else:
        imprimir_exito("Todos los productos superan ese limite de stock.")
        
def main():
    db_manager.inicializar_db()
    while True:
        print("\n" + "="*30)
        imprimir_titulo("GESTION DE INVENTARIO")
        print("="*30)
        print("1. Registrar Producto")
        print("2. Mostrar Productos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Buscar Producto")
        print("6. Reporte de Stock Bajo")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            menu_registrar()
        elif opcion == '2':
            menu_mostrar()
        elif opcion == '3':
            menu_actualizar()
        elif opcion == '4':
            menu_eliminar()
        elif opcion == '5':
            menu_buscar()
        elif opcion == '6':
            menu_reporte()
        elif opcion == '7':
            print("Saliendo del sistema. ¡Hasta luego!")
            sys.exit()
        else:
            imprimir_error("Opción inválida. Por favor, intente de nuevo.")
        
if __name__ == "__main__":
    main() 