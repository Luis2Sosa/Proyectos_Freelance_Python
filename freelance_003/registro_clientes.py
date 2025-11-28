
clientes = []

def registrar_clientes():
    nombre = input("Ingrese el nombre del cliente:\n").lower()

    try:
        telefono = int(input("Ingrese el telefono del cliente:\n"))
    except ValueError:
        print("Error: Ingrese un telefono valido.")
        return
    
    correo = input("Ingrese el correo del cliente:\n").lower()

    guardado = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo
    }

    clientes.append(guardado)
    print(f"Cliente '{nombre}' guardado correctamente.")

def buscar_cliente():
    nombre = input("Ingrese el nombre a buscar:\n").lower()

    encontrado = False

    for item in clientes:
        if nombre == item['nombre']:
            encontrado = True
            print(f"{item['nombre']} | Telefono: {item['telefono']} | Correo: {item['correo']}")
    
    if not encontrado:
        print(f"El cliente '{nombre}' No esta registrado.")

def mostrar_clientes():
    if not clientes:
        print("No hay clientes registrados. Ingrese a la opcion 1 para agregar un cliente.")

    for item in clientes:
        print(f"Nombre: {item['nombre']} | Telefono: {item['telefono']} | Correo: {item['correo']}")

print("=== BIENVENIDOS AL REGISTRO DE CLIENTES SM ===")

while True:
    print("=== MENU ===")
    print("1- Registrar cliente")
    print("2- Buscar cliente")
    print("3- Mostrar clientes")
    print("4- SALIR")

    try:
        opcion = int(input("Ingrese un numero de opcion:\n"))
    except ValueError:
        print("Error: Ingrese un numero de opcion valido.")
        continue

    if opcion == 1:
        registrar_clientes()
    elif opcion == 2:
        buscar_cliente()
    elif opcion == 3:
        mostrar_clientes()
    elif opcion == 4:
        print("--- Gracias por utilizar el registro SM ---")
        break
    else:
        print("Error: Ingrese una opcion del 1 al 4.")