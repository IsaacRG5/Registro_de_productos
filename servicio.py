# Agrega un producto al inventario
def agregar_producto(inventario, nombre, precio, cantidad):

    # Creamos un diccionario con los datos del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Guardamos el producto en la lista
    inventario.append(producto)

    print("Producto agregado correctamente")


# Muestra todos los productos del inventario
def mostrar_inventario(inventario):

    # Si el inventario está vacío se informa
    if not inventario:
        print("Inventario vacío")
        return

    # Recorremos la lista e imprimimos cada producto
    for p in inventario:
        print(p["nombre"], "| Precio:", p["precio"], "| Cantidad:", p["cantidad"])


# Busca un producto por su nombre
def buscar_producto(inventario, nombre):

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p

    return None


# Actualiza precio y cantidad de un producto
def actualizar_producto(inventario, nombre, precio, cantidad):

    producto = buscar_producto(inventario, nombre)

    if producto:
        producto["precio"] = precio
        producto["cantidad"] = cantidad
        print("Producto actualizado")
    else:
        print("Producto no encontrado")


# Elimina un producto del inventario
def eliminar_producto(inventario, nombre):

    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")


# Calcula estadísticas del inventario
def calcular_estadisticas(inventario):

    if not inventario:
        print("Inventario vacío")
        return None

    # Total de unidades
    unidades_totales = sum(p["cantidad"] for p in inventario)

    # Valor total del inventario
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    # Producto con mayor precio
    producto_caro = max(inventario, key=lambda p: p["precio"])

    # Producto con mayor cantidad
    producto_stock = max(inventario, key=lambda p: p["cantidad"])

    # Retornamos resultados en un diccionario
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_caro["nombre"],
        "producto_mayor_stock": producto_stock["nombre"]
    }