📋 Proyecto Freelance 009
Registro de Clientes con CRUD usando Archivos de Texto (Python)
📌 Descripción

Este proyecto es un sistema en consola desarrollado en Python que permite gestionar un registro de clientes utilizando archivos de texto (.txt) como almacenamiento persistente.

El sistema implementa un CRUD completo (Crear, Leer, Actualizar y Eliminar) sin utilizar bases de datos ni estructuras avanzadas, simulando cómo funcionan los sistemas reales cuando trabajan con archivos planos.

🎯 Objetivos del Proyecto

Practicar lógica backend real con persistencia de datos

Comprender cómo editar y eliminar registros en archivos de texto

Consolidar el patrón:

leer → reconstruir → sobrescribir

Fortalecer el pensamiento lógico más allá de la sintaxis

⚙️ Funcionalidades
1️⃣ Registrar cliente

Genera un ID automático incremental

Solicita:

Nombre

Teléfono

Correo

Guarda el cliente en clientes.txt

2️⃣ Ver clientes

Lee el archivo completo

Muestra todos los clientes registrados

Maneja archivo vacío o inexistente

3️⃣ Editar cliente por ID

Solicita un ID existente

Reconstruye el archivo:

Reemplaza solo la línea del cliente editado

Guarda los cambios sobrescribiendo el archivo

4️⃣ Eliminar cliente por ID

Solicita un ID

Reconstruye el archivo:

Excluye la línea del cliente eliminado

Guarda el archivo actualizado

5️⃣ Salir

Finaliza el programa de forma segura

🧠 Conceptos Clave Aprendidos

Manejo de archivos con open()

Uso de read(), readlines(), writelines()

Generación de ID incremental

Uso de listas como almacenamiento temporal

Flags (encontrado) para control de flujo

Manejo de errores con try / except

Persistencia de datos sin base de datos

📁 Estructura del Proyecto
freelance_009/
│
├── registro_clientes.py
├── clientes.txt
└── README.md

🚫 Restricciones

No se usan bases de datos

No se usan diccionarios ni listas como estructura final

Todo se guarda y se lee desde archivos .txt

🧪 Nivel del Proyecto

Junior Intermedio

Este proyecto simula escenarios reales de backend básico y prepara la base para trabajar luego con bases de datos.