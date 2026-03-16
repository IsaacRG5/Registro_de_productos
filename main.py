opcion = 0
inventario = []

while opcion <1 or opcion >4:
    print("""
    ----------bienvenido----------
        1. Agregar Producto
        2. Mostrar Inventario
        3. Calcular Estadisticas
        4. Salir
""")

    opcion = int(input("Que opcion deseas realizar: "))
    if opcion == "":
        print("Error opcipn no validad")




    if opcion == 1:
        print("\n=========Agregar producto=========")
        nombre_producto = input("Agregar el nombre del producto: ").isnumeric()
        if nombre_producto == "":
            print("Error: Opcion no validad")
        precio = float(input("Precio del producto: "))
        cantiadad = int(input("Cantidad de productos: "))
        
        

