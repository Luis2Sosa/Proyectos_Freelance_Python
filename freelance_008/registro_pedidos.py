

def mostrar_menu():
    print("=== MENU ===")
    print("1. Registrar pedido")
    print("2. Ver pedidos")
    print("3. Buscar pedido")
    print("4. SALIR")

def generar_id():
    try:
        with open("pedidos.txt", "r") as f:
            lineas = f.readlines()
            return len(lineas) + 1
    except FileNotFoundError:
        return 1
    
def registrar_pedido():
    nombre = input("Ingrese el nombre del cliente:\n").lower()

    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    
    producto = input("Ingrese el nombre del producto:\n").lower()

    if not producto:
        print("El producto no puede estar vacio.")
        return
    
    try:
        cantidad = int(input("Ingrese la cantidad de productos:\n"))
    except ValueError:
        print("Error: Ingrese un numero valido.")
        return
    try:
        precio = float(input("Ingrese el precio del producto:\n"))
    except ValueError:
        print("Error: Ingrese un precio valido.")
        return
    
    total = cantidad * precio

    id = generar_id()

    print("-- RESUMEN --")
    print(f"ID: {id} \nNombre: {nombre} \nProducto: {producto} \nCantidad: {cantidad} \nPrecio: {precio} \nTotal: {total}")
    print("--------------------------------------------------------------------------------------------------------------")

    confirmacion = input("Desea guardar el pedido? (s/n):\n").lower()

    if confirmacion == "s":
        with open("pedidos.txt", "a") as f:
            f.write(f"ID: {id} | Nombre: {nombre} | Producto: {producto} | Cantidad: {cantidad} | Precio: {precio} | Total: {total}\n")
            print("Pedido guardado correctamente.")
            print("--------------------------------------------------------------------------------------------------------------")

    elif confirmacion == "n":
        print("Pedido cancelado.")
        return
    
    else:
        print("Error: Ingrese una opcion valida.")
        return
    
def ver_pedidos():
    try:
        with open("pedidos.txt", "r") as f:
            datos = f.read()

            if not datos: 
                print("No hay pedidos registrados.")
                return
            
            print("-- PEDIDOS --")
            print(datos)
            print("--------------------------------------------------------------------------------------------------------------")
    
    except FileNotFoundError:
        print("No se encontro el pedido.")

def buscar_pedido():
    try:
        id_buscar = int(input("Ingrese el ID a buscar:\n"))
    except ValueError:
        print("Error: Ingrese un ID valido.")
        return
    
    try:
        with open("pedidos.txt", "r") as f:
            lineas = f.readlines()

            encontrado = False

            for linea in lineas:
                if f"ID: {id_buscar}" in linea:
                    print("PEDIDO ENCONTRADO")
                    print(linea)
                    encontrado = True
                    print("--------------------------------------------------------------------------------------------------------------")

            if not encontrado:
                print("No se encontro el pedido.")
                return
    
    except FileNotFoundError:
        print("No se ha encontrado el pedido.")

print("=== REGISTRO DE PEDIDOS ===")

while True:
    mostrar_menu()

    try:
        opcion = int(input("Ingrese un numero de opcion:\n"))
        print("--------------------------------------------------------------------------------------------------------------")
    except ValueError:
        print("Error: ingrese un numero de opcion valido.")
        continue

    if opcion == 1:
        registrar_pedido()
    elif opcion == 2:
        ver_pedidos()
    elif opcion == 3:
        buscar_pedido()
    elif opcion == 4:
        print("Hasta luego!")
        break
    else:
        print("Error: Ingrese una opcion del 1 al 4.")