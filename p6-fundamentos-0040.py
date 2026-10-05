# Hugo Fabian NC = 0040
# =====================================================================
# 1. PROGRAMACIÓN ORIENTADA A OBJETOS (Clase Carrito de Compras)
# =====================================================================
class Carrito:

    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(
            f"  [+] '{producto['nombre']}' añadido al carrito por ${producto['precio']:.2f}"
        )


# =====================================================================
# 2. BUCLES Y ESTRUCTURAS DE DATOS (Lista de productos)
# =====================================================================
# Datos de productos disponibles
catalogo = [
    {"nombre": "Laptop", "precio": 800.0, "stock": 3},
    {"nombre": "Mouse USB", "precio": 15.0, "stock": 0},  # Sin stock
    {"nombre": "Teclado", "precio": 45.0, "stock": 5},
    {"nombre": "Monitor", "precio": 150.0, "stock": 2},
]

# Crear el carrito del cliente
mi_carrito = Carrito("Carlos")
print(f"=== Procesando pedido para: {mi_carrito.cliente} ===")

# Recorrer el catálogo para intentar agregar cada producto
total_compra = 0

for prod in catalogo:
    nombre = prod["nombre"]
    precio = prod["precio"]
    stock = prod["stock"]

    # =================================================================
    # 3. ESTRUCTURA CONDICIONAL (Validación de Stock y Descuentos)
    # =================================================================
    if stock > 0:
        mi_carrito.agregar_producto(prod)
        total_compra += precio
    else:
        print(f"  [x] '{nombre}' no disponible (Agotado)")

# Evaluación de descuento según el monto total acumulado
print("\n--- Resumen de la Compra ---")
print(f"Subtotal: ${total_compra:.2f}")

if total_compra >= 500:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print(f"¡Descuento aplicado (10%): -${descuento:.2f}!")
    print(f"Total a pagar: ${total_final:.2f}")
elif total_compra > 0:
    print(f"Total a pagar: ${total_compra:.2f}")
else:
    print("El carrito está vacío.")
    
print("Hugo Fabian NC = 0040")
