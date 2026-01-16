

def mostrar_menu():
    print("=== MENU ===")
    print("1. Registrar cliente")
    print("2. Ver clientes")
    print("3. Editar cliente por ID")
    print("4. Borrar cliente por ID")
    print("5. SALIR")

def generar_id():
    try:
        with open("clientes.txt", "r") as f:
            lineas = f.readlines()
            return len(lineas) + 1
    except FileNotFoundError:
        return 1
    
def registrar_cliente():
    nombre = input("Ingrese el nombre del cliente:\n").lower()

    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    
    telefono = input("Ingrese el telefono del cliente:\n")

    if not telefono:
        print("El telefono no puede estar vacio.")
        return
    
    correo = input("Ingrese el correo del cliente:\n").lower()

    if not correo:
        print("El correo no puede estar vacio.")
        return
    
    id = generar_id()

    with open("clientes.txt", "a") as f:
        f.write(f"ID: {id} | Nombre: {nombre} | Telefono: {telefono} | Correo: {correo}\n")
        print("Cliente guardado correctamente.")
        print("---------------------------------------------------------------------------")

def ver_clientes():
    try:
        with open("clientes.txt", "r") as f:
            datos = f.read()

            if not datos:
                print("No hay clientes registrados.")
                return
            
            print("--- CLIENTES ---")
            print(datos)
            print("---------------------------------------------------------------------------")

    except FileNotFoundError:
        print("No se encontraron clientes.")

def editar_cliente():
    try:
        id_buscar = int(input("Ingrese el ID a editar:\n"))
    except ValueError:
        print("ID no valido.")
        return
    
    try:
        with open("clientes.txt", "r") as f:
            lineas = f.readlines()

            nueva_linea = []
            encontrado = False

            for linea in lineas:
                if f"ID: {id_buscar}" in linea:
                    print("Cliente encontrado.")

                    nuevo_nombre = input("Nuevo nombre:\n").lower()
                    nuevo_tel = input("Nuevo telefono:\n")
                    nuevo_correo = input("Nuevo correo:\n").lower()

                    nueva_linea.append(f"ID: {id_buscar} | Nombre: {nuevo_nombre} | Telefono: {nuevo_tel} | Correo: {nuevo_correo}\n")
                    encontrado = True
                else:
                    nueva_linea.append(linea)
            
            if not encontrado:
                print("No se encontro el cliente.")
                return
            
            with open("clientes.txt", "w") as f:
                f.writelines(nueva_linea)
            
            print("Cliente editado correctamente.")
    
    except FileNotFoundError:
        print("No se encontro el cliente.")

def eliminar_cliente():
    try:
        id_buscar = int(input("Ingrese el ID a eliminar:\n"))
    except ValueError:
        print("ID no valido.")
        return
    
    try:
        with open("clientes.txt", "r") as f:
            lineas = f.readlines()

            nueva_linea = []
            encontrado = False

            for linea in lineas:
                if f"ID: {id_buscar}" in linea:
                    encontrado = True
                else:
                    nueva_linea.append(linea)
            
            if not encontrado:
                print("No se encontro el cliente.")
                return
            
            with open("clientes.txt", "w") as f:
                f.writelines(nueva_linea)

            print("Cliente eliminado correctamente.")
    
    except FileNotFoundError:
        print("Cliente no encontrado.")

while True:
    mostrar_menu()

    try:
        opcion = int(input("Ingrese un numero de opcion:\n"))
        print("---------------------------------------------------------------------------")
    except ValueError:
        print("Opcion no valida.")
        continue

    if opcion == 1:
        registrar_cliente()
    elif opcion == 2:
        ver_clientes()
    elif opcion == 3:
        editar_cliente()
    elif opcion == 4:
        eliminar_cliente()
    elif opcion == 5:
        print("Hasta luego.")
        break
    else:
        print("Error: Ingrese una opcion del 1 al 5.")
