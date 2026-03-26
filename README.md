# 📦 Sistema de Inventario en Python

Aplicación de consola desarrollada en Python para gestionar un inventario de productos. Permite agregar, buscar, actualizar, eliminar productos, generar estadísticas y manejar archivos CSV de forma segura.

---

## 🚀 Funcionalidades

- Agregar productos al inventario  
- Mostrar todos los productos  
- Buscar productos por nombre  
- Actualizar precio y cantidad  
- Eliminar productos  
- Generar estadísticas:
  - Total de unidades
  - Valor total del inventario
  - Producto más caro
  - Producto con mayor stock  
- Guardar inventario en archivo CSV  
- Cargar inventario desde CSV  
- Sobrescribir o fusionar inventario  
- Manejo de errores (datos inválidos, archivos corruptos, etc.)

---

## 🧠 Tecnologías utilizadas

- Python 3  
- Módulo `csv`  
- Programación estructurada  
- Manejo de excepciones (`try/except`)


## Estructura del proyecto
inventario/
│
├── main.py
├── servicio.py
├── archivos.py
└── README.md

## Ejemplo de uso
====== SISTEMA DE INVENTARIO ======
1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Ver estadísticas
7. Guardar inventario en CSV
8. Cargar inventario desde CSV
9. Salir

## Manejo de errores

El sistema está diseñado para no fallar:

Si ingresas datos incorrectos → muestra error
Si el archivo no existe → muestra mensaje
Si el CSV tiene errores → ignora filas inválidas
El programa nunca se cierra inesperadamente

## Manejo de archivos CSV
Guardar
*Guarda productos en formato .csv
*Incluye encabezados automáticamente
Cargar
*Valida estructura del archivo
*Ignora filas incorrectas
*Muestra cuántos datos se cargaron correctamente
*Reporta filas inválidas
Fusión
*Si el producto ya existe → suma la cantidad
*Si no existe → lo agrega

---
### Link al repositorio: [SystemInvertory](https://github.com/IsaacRG5/Registro_de_productos.git)
El Codigo esta en feature/2-codigo

## ▶️ Ejecución

1. Abre el proyecto en Visual Studio Code  
2. Ejecuta el archivo:

```bash
python main.py

