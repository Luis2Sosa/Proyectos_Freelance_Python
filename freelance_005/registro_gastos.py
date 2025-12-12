
gastos = []

def registrar_gasto():
    nombre = input("Ingrese el nombre del gasto:\n").lower()

    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    
    try:
        monto = int(input("Ingrese el monto:\n"))
    except ValueError:
        print("Error: Ingrese un monto valido.")
        return
    
    categoria = input("Ingrese la categoria:\n").lower()
    print("------------------------------------------")

    if not categoria:
        print("La categoria no puede estar vacia.")
        return
    
    gasto = {
        "nombre": nombre,
        "monto": monto,
        "categoria": categoria,
        "estado": "Pendiente"
    }

    gastos.append(gasto)
    print(f"Gasto '{nombre}' agregado correctamente.")
    print("------------------------------------------")

def mostrar_gastos():
    if not gastos:
        print("No hay gastos registrados.")
        return
    
    for item in gastos:
        print(f"Nombre: {item['nombre']} \nMonto: RD${item['monto']} \nCategoria: {item['categoria']} \nEstado: {item['estado']}")
        print("------------------------------------------")

def buscar_gasto():
    nombre = input("Ingrese el nombre del gasto a buscar:\n").lower()
    print("------------------------------------------")

    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    
    encontrado = False

    for item in gastos:
        if nombre == item['nombre']:
            encontrado = True
            print(f"Nombre: {item['nombre']} \nMonto: RD${item['monto']} \nCategoria: {item['categoria']} \nEstado: {item['estado']}")
            print("------------------------------------------")

    if not encontrado:
        print(f"Gasto '{nombre}' no encontrado.")

def marcar_pagado():
    nombre = input("Ingrese el nombre del gasto a pagar:\n").lower()
    print("------------------------------------------")

    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    
    encontrado = False

    for item in gastos:
        if nombre == item['nombre']:
            encontrado = True
            item['estado'] = "Pagado"
            print(f"Gasto '{nombre}' pagado correctamente.")
            print("------------------------------------------")
            return
    
    if not encontrado:
        print(f"Gasto '{nombre}' no encontrado.")

def eliminar_gasto():
    nombre = input("Ingrese el nombre del gasto a eliminar:\n").lower()
    print("------------------------------------------")

    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    
    encontrado = False

    for item in gastos:
        if nombre == item['nombre']:
            encontrado = True
            gastos.remove(item)
            print(f"Gasto '{nombre}' eliminado correctamente.")
            print("------------------------------------------")
            return
    
    if not encontrado:
        print(f"Gasto '{nombre}' no encontrado.")

def calcular_total():
    if not gastos:
        print("No hay gastos registrados.")
    
    total_pagado = 0

    for item in gastos:
        if item['estado'] == "Pagado":
            total_pagado += item['monto']
    print(f"El total pagado es: {total_pagado}")
    print("------------------------------------------")

print("=== BIENVENIDOS AL REGISTRO DE PAGOS PERSONALES ===")

while True:
    print("=== MENU ===")
    print("1- Registrar gasto")
    print("2- Mostrar gastos")
    print("3- Buscar gasto")
    print("4- Marcar gasto como pagado")
    print("5- Eliminar gasto")
    print("6- Calcular total pagado")
    print("7- SALIR")

    try:
        opcion = int(input("Ingrese un numero de opcion:\n"))
        print("------------------------------------------")
    except ValueError:
        print("Error: Ingrese un numero valido.")
        continue

    if opcion == 1:
        registrar_gasto()
    elif opcion == 2:
        mostrar_gastos()
    elif opcion == 3:
        buscar_gasto()
    elif opcion == 4:
        marcar_pagado()
    elif opcion == 5:
        eliminar_gasto()
    elif opcion == 6:
        calcular_total()
    elif opcion == 7:
        print("--- Gracias por utilizar el registro de gastos personales ---")
        break
    else:
        print("Error: Favor de elegir una opcion del 1 al 7 e intentelo de nuevo.")