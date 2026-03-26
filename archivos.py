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
import csv

# Carga inventario desde un archivo CSV
def cargar_csv(ruta):

    inventario = []
    errores = 0

    try:
        with open(ruta, newline="", encoding="utf-8") as archivo:

            reader = csv.reader(archivo)

            # Intentamos leer el encabezado
            try:
                header = next(reader)
            except StopIteration:
                print("Error: El archivo está vacío o corrupto")
                return []

            # Validamos encabezado
            if header != ["nombre", "precio", "cantidad"]:
                print("Error: Encabezado incorrecto")
                return []

            # Procesamos cada fila
            for fila in reader:

                # Validamos estructura de la fila
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
                    # Si no se puede convertir a número
                    errores += 1

        # Reporte final (MUY IMPORTANTE)
        print("Productos cargados correctamente:", len(inventario))
        print("Filas inválidas u omitidas:", errores)

        return inventario

    except FileNotFoundError:
        print("Error: Archivo no encontrado")

    except UnicodeDecodeError:
        print("Error: El archivo tiene problemas de codificación")

    except Exception as e:
        # Captura cualquier error inesperado (archivo corrupto, etc.)
        print("Error inesperado al cargar el archivo:", e)

    # Nunca dejamos que el programa se rompa
    return []