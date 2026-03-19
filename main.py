from funciones import *

# Programa principal
def main():
    opcion = 0
    inventario = []

    while opcion != 4:
        mostrar_menu()

        try:
            opcion = int(input("Que opcion deseas realizar: "))
        except ValueError:
            print("Error: Opcion no valida, ingrese un numero.")
            continue

        if opcion < 1 or opcion > 4:
            print("Error: Debe ingresar una opcion entre 1 y 4")
            continue

        if opcion == 1:
            agregar_producto(inventario)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            calcular_estadisticas(inventario)

    print("\nPrograma finalizado")


# Ejecutar programa
main() 