# Importamos las funciones de los otros archivos
from servicio import *
from archivos import *


# Función que muestra el menú principal
def mostrar_menu():
    print("\n====== SISTEMA DE INVENTARIO ======")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Ver estadísticas")
    print("7. Guardar inventario en CSV")
    print("8. Cargar inventario desde CSV")
    print("9. Salir")


# Función principal del programa
def main():

    inventario = []  # Lista donde se guardan los productos
    opcion = 0       # Variable que almacena la opción del menú

    # El programa se ejecuta hasta que el usuario elija salir
    while opcion != 9:

        mostrar_menu()

        # Intentamos convertir la opción a número
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: ingrese un número válido")
            continue

        # -------- OPCIÓN 1: AGREGAR PRODUCTO --------
        if opcion == 1:

            nombre = input("Nombre del producto: ")

            # Validamos precio y cantidad
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                if precio < 0 or cantidad < 0:
                    print("El precio y la cantidad deben ser positivos")
                    continue
            except ValueError:
                print("Datos inválidos")
                continue

            # Llamamos la función que agrega el producto
            agregar_producto(inventario, nombre, precio, cantidad)

        # -------- OPCIÓN 2: MOSTRAR INVENTARIO --------
        elif opcion == 2:
            mostrar_inventario(inventario)

        # -------- OPCIÓN 3: BUSCAR PRODUCTO --------
        elif opcion == 3:

            nombre = input("Producto a buscar: ")
            producto = buscar_producto(inventario, nombre)

            if producto:
                print("Producto encontrado:", producto)
            else:
                print("Producto no encontrado")

        # -------- OPCIÓN 4: ACTUALIZAR PRODUCTO --------
        elif opcion == 4:

            nombre = input("Producto a actualizar: ")

            try:
                precio = float(input("Nuevo precio: "))
                cantidad = int(input("Nueva cantidad: "))
            except ValueError:
                print("Datos inválidos")
                continue

            actualizar_producto(inventario, nombre, precio, cantidad)

        # -------- OPCIÓN 5: ELIMINAR PRODUCTO --------
        elif opcion == 5:

            nombre = input("Producto a eliminar: ")
            eliminar_producto(inventario, nombre)

        # -------- OPCIÓN 6: ESTADÍSTICAS --------
        elif opcion == 6:

            stats = calcular_estadisticas(inventario)

            if stats:
                print("\n--- ESTADÍSTICAS ---")
                print("Unidades totales:", stats["unidades_totales"])
                print("Valor total:", stats["valor_total"])
                print("Producto más caro:", stats["producto_mas_caro"])
                print("Mayor stock:", stats["producto_mayor_stock"])

        # -------- OPCIÓN 7: GUARDAR CSV --------
        elif opcion == 7:

            ruta = input("Nombre del archivo CSV: ")
            guardar_csv(inventario, ruta)

        # -------- OPCIÓN 8: CARGAR CSV --------
        elif opcion == 8:

            ruta = input("Nombre del archivo CSV: ")
            datos = cargar_csv(ruta)

            if datos:

                # Preguntamos si se quiere reemplazar o fusionar inventario
                respuesta = input("¿Sobrescribir inventario actual? (S/N): ")

                if respuesta.upper() == "S":
                    inventario = datos
                    print("Inventario reemplazado")

                else:
                    # Fusionamos inventarios
                    for nuevo in datos:

                        existente = buscar_producto(inventario, nuevo["nombre"])

                        if existente:
                            # Si ya existe, se suma la cantidad
                            existente["cantidad"] += nuevo["cantidad"]
                            existente["precio"] = nuevo["precio"]
                        else:
                            # Si no existe, se agrega
                            inventario.append(nuevo)

                    print("Inventario fusionado")

    print("Programa finalizado")


# Ejecutamos el programa
main()