# Sistema de Inventario

---

##  Descripción

Este sistema permite gestionar un inventario de productos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

El programa está desarrollado en Python y permite:

- Agregar, buscar, actualizar y eliminar productos
- Visualizar el inventario
- Calcular estadísticas del negocio
- Guardar y cargar información usando archivos CSV

El inventario se almacena en memoria utilizando listas y diccionarios, y se puede persistir en archivos para conservar los datos entre sesiones.

---

##  Características

- ✔ Operaciones CRUD completas
- ✔ Uso de listas y diccionarios
- ✔ Persistencia de datos en archivos CSV
- ✔ Cálculo de estadísticas del inventario
- ✔ Validación de datos y manejo de errores
- ✔ Código modular organizado en varios archivos

---

##  Estructura del proyecto
inventario/
│
├── app.py
├── servicios.py
├── archivos.py
└── README.md


## Menú del sistema

El programa cuenta con las siguientes opciones:

Agregar producto
Mostrar inventario
Buscar producto
Actualizar producto
Eliminar producto
Ver estadísticas
Guardar inventario en CSV
Cargar inventario desde CSV
Salir

## Persistencia en CSV

El sistema permite guardar el inventario en un archivo CSV con el siguiente formato:

nombre,precio,cantidad
arroz,2500,10
leche,3000,5
pan,800,20

También permite cargar archivos CSV validando:

Encabezado correcto
Número de columnas
Tipo de datos (float e int)
Valores no negativos

Las filas inválidas son omitidas y reportadas.

##  Estructura de datos

Cada producto se representa como un diccionario:

```python
{
    "nombre": "producto",
    "precio": 1000.0,
    "cantidad": 5
}
