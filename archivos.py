import csv


# Guarda el inventario en un archivo CSV
def guardar_csv(inventario, ruta, incluir_header=True):

    # Verificamos que haya productos
    if not inventario:
        print("Inventario vacío")
        return

    try:

        # Abrimos el archivo en modo escritura
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:

            writer = csv.writer(archivo)

            # Escribimos encabezado
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            # Escribimos cada producto
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print("Inventario guardado en:", ruta)

    except Exception as e:
        print("Error al guardar:", e)


# Carga inventario desde un archivo CSV
def cargar_csv(ruta):

    inventario = []
    errores = 0

    try:

        with open(ruta, newline="", encoding="utf-8") as archivo:

            reader = csv.reader(archivo)

            # Leemos encabezado
            header = next(reader)

            # Validamos encabezado
            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado incorrecto")
                return []

            # Procesamos cada fila
            for fila in reader:

                if len(fila) != 3:
                    errores += 1
                    continue

                try:

                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    # Validamos valores negativos
                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except ValueError:
                    errores += 1

        print("Productos cargados:", len(inventario))
        print("Filas inválidas omitidas:", errores)

        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado")

    except UnicodeDecodeError:
        print("Error al leer archivo")

    return []