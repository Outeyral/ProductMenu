products = []  # Lista de productos

def agregar_producto():
    global counter
    print("\n--- AGREGAR PRODUCTO ---")
    
    while True:
        name = input("Nombre del producto: ").strip().capitalize()
        if name:
            break
        print("El nombre no puede estar vacío.")

    while True:
        category = input("Categoría del producto: ").strip().capitalize()
        if category:
            break
        print("La categoría no puede estar vacía.")

    while True:
        try:
            price = int(input("Precio (entero, sin centavos): "))
            if price > 0:
                break
            print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Por favor, ingresá un número válido.")

    products.append([name, category, price])
    print(f"\n✅ Producto '{name}' agregado.")

def ver_productos():
    print("\n--- LISTA DE PRODUCTOS ---")
    if not products:
        print("No hay productos cargados.")
        return
    for idx, p in enumerate(products):
        print(f"{idx+1}: Nombre: {p[0]}, Categoría: {p[1]}, Precio: ${p[2]}")

def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    if not products:
        print("No hay productos para eliminar.")
        return
    ver_productos()
    while True:
        try:
            index = int(input("\nIngresá el número del producto a eliminar: "))
            index -= 1
            if 0 <= index < len(products):
                eliminado = products.pop(index)
                print(f"✅ Producto '{eliminado[0]}' eliminado.")
                break
            print("Índice inválido.")
        except ValueError:
            print("Ingresá un número válido.")

def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")
    if not products:
        print("No hay productos para buscar.")
        return
    nombre = input("Nombre a buscar: ").strip().capitalize()
    encontrados = [p for p in products if nombre in p[0]]
    if encontrados:
        for p in encontrados:
            print(f"Nombre: {p[0]}, Categoría: {p[1]}, Precio: ${p[2]}")
    else:
        print("No se encontraron productos con ese nombre.")

# --- Menú principal ---
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1 - Agregar producto")
    print("2 - Ver productos")
    print("3 - Eliminar producto")
    print("4 - Buscar producto")
    print("5 - Salir")

    opcion = input("Elegí una opción (1-5): ").strip()

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        ver_productos()
    elif opcion == '3':
        eliminar_producto()
    elif opcion == '4':
        buscar_producto()
    elif opcion == '5':
        print("\n👋 ¡Gracias por usar el gestor de productos!")
        break
    else:
        print("❌ Opción inválida. Probá de nuevo.")