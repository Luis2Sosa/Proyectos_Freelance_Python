
tareas = []

def registrar_tarea():
    titulo = input("Ingrese el titulo de la tarea:\n")
    print("-------------------------------------------------")

    if not titulo:
        print("El titulo no puede estar vacio.")
        return
    
    descripcion = input("Ingrese la descripcion de la tarea:\n")

    if not descripcion:
        print("La descripcion no puede estar vacia.")
        return
    
    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "estado": "Pendiente"
    }

    tareas.append(tarea)
    print(f"Tarea '{titulo}' agregada correctamente.")
    print("-------------------------------------------------")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    for item in tareas:
        print(f"Titulo: {item['titulo']} \nDescripcion: {item['descripcion']} \nEstado: {item['estado']}")
        print("-------------------------------------------------")

def buscar_tarea():
    titulo = input("Ingrese el titulo de la tarea a buscar:\n")
    print("-------------------------------------------------")

    encontrado = False

    for item in tareas:
        if titulo == item['titulo']:
            encontrado = True
            print(f"Titulo: {item['titulo']} \nDescripcion: {item['descripcion']} \nEstado: {item['estado']}")
            print("-------------------------------------------------")

    if not encontrado:
        print(f"Tarea '{titulo}' no encontrada")

def completar_tarea():
    titulo = input("Ingrese el titulo de la tarea a completar:\n")
    print("-------------------------------------------------")

    encontrado = False

    for item in tareas:
        if titulo == item['titulo']:
            encontrado = True
            item['estado'] = "Completada"
            print(f"Tarea '{titulo}' completada correctamente.")
    
    if not encontrado:
        print(f"Tarea '{titulo}' no encontrada")

def editar_tarea():
    titulo = input("Ingrese el titulo de la tarea a editar:\n")
    print("-------------------------------------------------")

    encontrado = False

    for item in tareas:
        if titulo == item['titulo']:
            encontrado = True

            nuevo_titulo = input("Ingrese el nuevo titulo:\n")
            nueva_descripcion = input("Ingrese la nueva descripcion:\n")
            nuevo_estado = input("Ingrese el nuevo estado (Pendiente / Completada):\n")

            item['titulo'] = nuevo_titulo
            item['descripcion'] = nueva_descripcion
            item['estado'] = nuevo_estado
            print("Tarea editada correctamente.")
            print("-------------------------------------------------")

    if not encontrado:
        print(f"Tarea '{titulo}' no encontrada")
    
def eliminar_tarea():
    titulo = input("Ingrese el titulo de la tarea a eliminar:\n")
    print("-------------------------------------------------")

    encontrado = False

    for item in tareas:
        if titulo == item['titulo']:
            encontrado = True
            tareas.remove(item)
            print(f"Tarea '{titulo}' eliminada correctamente.")
            print("-------------------------------------------------")

    if not encontrado:
        print(f"Tarea '{titulo}' no encontrada")
        

print("=== BIENVENIDOS AL REGISTRO DE TAREAS ===")

while True:
    print("=== MENU ===")
    print("1- Registrar tarea")
    print("2- Mostrar tareas")
    print("3- Buscar tarea")
    print("4- Completar tarea")
    print("5- Editar tarea")
    print("6- Eliminar tarea")
    print("7- SALIR")

    try:
        opcion = int(input("Ingrese un numero de opcion:\n"))
        print("-------------------------------------------------")
    except ValueError:
        print("Error: Ingrese un numero valido.")
        continue

    if opcion == 1:
        registrar_tarea()
    elif opcion == 2:
        mostrar_tareas()
    elif opcion == 3:
        buscar_tarea()
    elif opcion == 4:
        completar_tarea()
    elif opcion == 5:
        editar_tarea()
    elif opcion == 6:
        eliminar_tarea()
    elif opcion == 7:
        print("--- GRACIAS POR UTILIZAR EL REGISTRO DE TAREAS ---")
        break
    else:
        print("Error: Opcion no valida. Ingrese un numero del 1 al 7.")