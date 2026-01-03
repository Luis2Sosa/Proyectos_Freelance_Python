📦 Proyecto Freelance 008

Registro de pedidos con ID automático y búsqueda

📌 Descripción

Este proyecto es un sistema en consola desarrollado en Python que permite registrar pedidos, asignarles un ID único automático, almacenarlos en un archivo de texto y consultarlos posteriormente mediante búsquedas por ID.

No utiliza bases de datos. Toda la información se guarda en archivos .txt, simulando un sistema de persistencia real de datos.

⚙️ Funcionalidades

Registrar pedidos con ID automático

Guardar pedidos en archivo pedidos.txt

Ver todos los pedidos registrados

Buscar pedidos por su ID

Validación de datos de entrada

Manejo de errores con try / except

Menú interactivo en consola

🧠 ¿Cómo funciona?

Cada pedido se guarda como una línea dentro del archivo pedidos.txt

El ID se genera automáticamente contando las líneas existentes en el archivo

El siguiente pedido recibe el número consecutivo

La búsqueda se realiza leyendo el archivo línea por línea y comparando el ID

🗂️ Estructura del proyecto
freelance_008/
│
├── registro_pedidos.py
├── pedidos.txt
└── notas.txt

▶️ Cómo ejecutar

Desde la carpeta del proyecto, ejecuta:

python registro_pedidos.py

🧪 Nivel

Junior Intermedio

📅 Estado

Proyecto funcional desarrollado desde cero como parte de una serie de proyectos freelance enfocados en fortalecer la lógica, manejo de archivos y control de flujo en Python.

✍️ Autor

Luis Sosa