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

##  Estructura de datos

Cada producto se representa como un diccionario:

```python
{
    "nombre": "producto",
    "precio": 1000.0,
    "cantidad": 5
}