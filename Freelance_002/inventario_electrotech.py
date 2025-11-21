
inventario = []

print("=== Bienvenidos a electrotech 🖥️ ===")
print("--- Escriba 'fin' para finalizar ---")

while True:
    nombre = input("Ingrese el nombre del producto:\n")
    if nombre.lower() == 'fin':
        break

    try:
        cantidad = int(input("Ingrese la cantidad de producto:\n"))
    except ValueError:
        print("Error: Ingrese un numero valido")
        continue
    
    try:
        precio = int(input("Ingrese el precio del producto:\n"))
    except ValueError:
        print("Error: Ingrese un precio valido")
        continue

    productos = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(productos)

productos_vendidos = len(inventario)
total = 0

print("=== INVENTARIO ===")
for item in inventario:
    subtotal = item['precio'] * item['cantidad']
    total += subtotal
    print(f"{item['nombre']} | Cantidad: {item['cantidad']} | Precio: RD${item['precio']} | Subtotal: {subtotal}")

print(f"Productos vendidos: {productos_vendidos}")
print(f"Total recaudado: {total}")

if total >= 500:
    print("Hoy fue un excelente dia!")
else:
    print("Mañana sera un mejor dia.")

