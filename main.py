opcion = 0
inventario = []

while opcion != 4:

    print("""
    ----------bienvenido----------
        1. Agregar Producto
        2. Mostrar Inventario
        3. Calcular Estadisticas
        4. Salir
    """)

    try:
        opcion = int(input("Que opcion deseas realizar: "))
    except ValueError:
        print("Error: Opcion no valida, ingrese un numero.")
        continue

    if opcion < 1 or opcion > 4:
        print("Error: Debe ingresar una opcion entre 1 y 4")
        continue

    if opcion == 1:

        nombre_producto = ""

        while nombre_producto.lower() != "salir":

            print("\n=========Agregar producto=========")
            nombre_producto = input("Agregar el nombre del producto (escribe 'salir' para terminar): ")

            if nombre_producto.lower() != "salir":

                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad de productos: "))

                producto = {
                    "nombre del producto": nombre_producto,
                    "precio": precio,
                    "cantidad": cantidad
                }

                inventario.append(producto)

                print("Producto agregado correctamente")

    elif opcion == 2:

        if not inventario:
            print("\nEl inventario está vacío")

        else:
            print("\nInventario registrado:\n")

            for i, producto in enumerate(inventario, start=1):
                print(f"{i}. Producto: {producto['nombre del producto']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

    elif opcion == 3:

        if not inventario:
            print("\nNo hay productos para calcular estadísticas")

        else:
            valor_total = 0
            cantidad_total = 0

            for producto in inventario:
                valor_total += producto["precio"] * producto["cantidad"]
                cantidad_total += producto["cantidad"]

            print("\n===== Estadísticas =====")
            print(f"Valor total del inventario: {valor_total}")
            print(f"Cantidad total de productos: {cantidad_total}")

print("\nPrograma finalizado")