# Lista para guardar los productos
productos = []

#  Bienvenida e instrucciones
print("=== BIENVENIDA AL SISTEMA DE CALCULOS ===")
print("--- Acuerde escribir 'FIN' al final de la jornada para completar los calculos totales ---")

# Bucle para ejecutar hasta salir
while True:
    nombre = input("Ingrese el nombre del producto:\n")
    if nombre == "FIN":
        break
    precio = int(input("Ingrese el precio del producto:\n"))
    productos.append(precio)
    

total = sum(productos)
cantidad = len(productos)

print(f"Hoy se vendieron {cantidad} productos, y la venta total del dia fue {total}")
