---

# 📁 **Proyecto 003 – Sistema de Registro de Clientes (Freelance Python)**

Este proyecto consiste en un **sistema básico de registro de clientes**, diseñado como práctica freelance para mejorar habilidades en lógica, estructuras de datos y manejo de menús interactivos en consola.

El programa permite:

* Registrar clientes
* Buscar clientes por nombre
* Mostrar todos los clientes registrados
* Manejar errores de entrada del usuario
* Crear un flujo de menú profesional, similar a sistemas reales de negocios

---

## 🧩 **Características principales**

### ✔ Registrar clientes

El sistema solicita:

* Nombre
* Teléfono (validado como número)
* Correo

Los datos se guardan en un diccionario y se almacenan dentro de una lista principal.

### ✔ Buscar un cliente

* El usuario escribe el nombre.
* El sistema recorre la lista completa.
* Si lo encuentra, muestra su información.
* Si no existe, indica que el cliente no está registrado.

### ✔ Mostrar todos los clientes

* Si no hay clientes, muestra un mensaje informativo.
* Si los hay, imprime cada cliente con su información formateada.

### ✔ Validación de datos

Se utiliza `try/except` para evitar errores cuando el usuario introduce texto en campos numéricos.

### ✔ Menú interactivo profesional

Incluye opciones claras con un bucle `while True` que se ejecuta hasta que el usuario selecciona SALIR.

---

## 📂 **Tecnologías utilizadas**

* Python 3
* Estructuras de datos: listas y diccionarios
* Manejo de excepciones
* Entrada de datos por consola

---

## ▶ **Cómo ejecutar**

1. Abrir el archivo `registro_clientes.py`
2. Ejecutarlo con:

```bash
python registro_clientes.py
```

3. Usar el menú para registrar, buscar o mostrar clientes.

---

## 🎯 **Objetivo del proyecto**

Este proyecto forma parte del **Curso Freelance Python**, donde cada ejercicio simula un trabajo real.
El objetivo es desarrollar habilidades profesionales creando soluciones completas desde cero.

---

## 👨‍💻 **Autor**

Luis Sosa – Proyecto creado como práctica real de programación freelance.

---

