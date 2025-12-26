
def mostrar_menu():
    print("=== MENU ===")
    print("1- Registrar pedido")
    print("2- Ver pedidos")
    print("3- Salir")

def registrar_pedido():
    nombre = input("Ingrese el nombre del usuario:\n").lower()

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

    print("=== RESUMEN ===")
    print(f"Nombre: {nombre} \nProducto: {producto} \nCantidad: {cantidad} \nPrecio: {precio} \nTotal: {total}")
    print("----------------------------------------------------------------------------------------------------")

    confirmacion = input("Desea guardar el pedido? (s/n):\n").lower()

    if confirmacion == "s":
        with open("pedidos.txt", "a") as f:
            f.write(f"Nombre: {nombre} | Producto: {producto} | Cantidad: {cantidad} | Precio: {precio} | Total: {total}\n")
            print("Pedido guardado correctamente.")
            print("----------------------------------------------------------------------------------------------------")
    
    elif confirmacion == "n":
        print("Pedido cancelado.")
        return
    
    else:
        print("Error: Opcion no valida.")
        return
    
def ver_pedidos():
    try:
        with open("pedidos.txt", "r") as f:
            datos = f.read()

            if not datos:
                print("No hay pedidos registrados.")
                return
            
            print("=== PEDIDOS ===")
            print(datos)
            print("----------------------------------------------------------------------------------------------------")
    
    except FileNotFoundError:
        print("Error: No se encontro el pedido.")
        return
    
print("=== REGISTRO DE PEDIDOS ===")

while True:
    mostrar_menu()

    try:
        opcion = int(input("Ingrese un numero de opcion:\n"))
        print("----------------------------------------------------------------------------------------------------")
    except ValueError:
        print("Error: Ingrese una opcion valida.")
        continue

    if opcion == 1:
        registrar_pedido()
    elif opcion == 2:
        ver_pedidos()
    elif opcion == 3:
        print("Hasta luego!")
        break
    else:
        print("Error: Ingrese una opcion del 1 al 3.")