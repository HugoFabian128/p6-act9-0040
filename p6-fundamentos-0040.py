# Hugo Fabian NC = 0040
# =====================================================================
# 1. VARIABLES BÁSICAS (python_variables.asp)
# =====================================================================

# Ej 1.1: Creación de variables de texto y numéricas
nombre_usuario = "Carlos"
edad_usuario = 28
print("=== 1.1 Variables Básicas ===")
print(f"Usuario: {nombre_usuario}")
print(f"Edad: {edad_usuario}\n")

# Ej 1.2: Cambio de tipo de dato (tipado dinámico)
variable_flexible = 100
print("=== 1.2 Tipado Dinámico ===")
print(f"Valor inicial (entero): {variable_flexible}")
variable_flexible = "Ahora soy un texto"
print(f"Valor modificado (string): {variable_flexible}\n")

# Ej 1.3: Forzado de tipos (Casting explícito)
precio_texto = "15"
precio_numero = int(precio_texto)
print("=== 1.3 Casting de Variables ===")
print(f"Texto convertido a entero: {precio_numero}")
print(f"Resultado de sumar 5: {precio_numero + 5}\n")


# =====================================================================
# 2. ASIGNACIÓN MÚLTIPLE (python_variables_multiple.asp)
# =====================================================================

# Ej 2.1: Múltiples valores a múltiples variables
x, y, z = "Manzana", "Banana", "Naranja"
print("=== 2.1 Asignación Múltiple ===")
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}\n")

# Ej 2.2: Un mismo valor a múltiples variables
valor_a = valor_b = valor_c = 0
print("=== 2.2 Un mismo valor a varias variables ===")
print(f"a: {valor_a}")
print(f"b: {valor_b}")
print(f"c: {valor_c}\n")

# Ej 2.3: Desempaquetado de listas (Unpacking)
coordenadas = [19.4326, -99.1332]
latitud, longitud = coordenadas
print("=== 2.3 Desempaquetado (Unpacking) ===")
print(f"Latitud: {latitud}")
print(f"Longitud: {longitud}\n")


# =====================================================================
# 3. TIPOS DE DATOS (python_datatypes.asp)
# =====================================================================

# Ej 3.1: Tipos numéricos (int, float, complex)
entero = 10
decimal = 3.1416
complejo = 2 + 3j
print("=== 3.1 Tipos Numéricos ===")
print(f"Entero ({entero}): {type(entero)}")
print(f"Decimal ({decimal}): {type(decimal)}")
print(f"Complejo ({complejo}): {type(complejo)}\n")

# Ej 3.2: Colecciones (str, list, tuple, dict)
lista_colores = ["rojo", "verde", "azul"]
tuple_dimensiones = (1920, 1080)
diccionario_persona = {"nombre": "Ana", "edad": 25}
print("=== 3.2 Colecciones ===")
print(f"Lista: {type(lista_colores)}")
print(f"Tupla: {type(tuple_dimensiones)}")
print(f"Diccionario: {type(diccionario_persona)}\n")

# Ej 3.3: Booleanos y Conjuntos (bool, set)
es_activo = True
conjunto_ids = {101, 102, 103}
print("=== 3.3 Booleanos y Conjuntos ===")
print(f"Booleano ({es_activo}): {type(es_activo)}")
print(f"Set ({conjunto_ids}): {type(conjunto_ids)}\n")


# =====================================================================
# 4. OPERADORES ARITMÉTICOS (python_operators_arithmetic.asp)
# =====================================================================

# Ej 4.1: Suma, Resta y Multiplicación
num1, num2 = 12, 5
print("=== 4.1 Suma, Resta y Multiplicación ===")
print(f"Suma (12 + 5): {num1 + num2}")
print(f"Resta (12 - 5): {num1 - num2}")
print(f"Multiplicación (12 * 5): {num1 * num2}\n")

# Ej 4.2: División exacta, entera y módulo
print("=== 4.2 Divisiones y Módulo ===")
print(f"División exacta (12 / 5): {num1 / num2}")
print(f"División entera (12 // 5): {num1 // num2}")
print(f"Módulo / Residuo (12 % 5): {num1 % num2}\n")

# Ej 4.3: Exponenciación / Potencia
base, exponente = 2, 3
potencia = base ** exponente
print("=== 4.3 Exponenciación ===")
print(f"Potencia (2 ** 3): {potencia}\n")


# =====================================================================
# 5. OPERADORES DE COMPARACIÓN (python_operators_comparison.asp)
# =====================================================================

# Ej 5.1: Igualdad y Desigualdad
a, b = 15, 20
print("=== 5.1 Igualdad y Desigualdad ===")
print(f"¿15 == 20?: {a == b}")
print(f"¿15 != 20?: {a != b}\n")

# Ej 5.2: Mayor que y Menor que
print("=== 5.2 Mayor que y Menor que ===")
print(f"¿15 > 20?: {a > b}")
print(f"¿15 < 20?: {a < b}\n")

# Ej 5.3: Mayor o igual / Menor o igual
limite, valor = 10, 10
print("=== 5.3 Mayor/Menor o Igual ===")
print(f"¿10 >= 10?: {valor >= limite}")
print(f"¿10 <= 10?: {valor <= limite}\n")


# =====================================================================
# 6. OPERADORES LÓGICOS (python_operators_logical.asp)
# =====================================================================

# Ej 6.1: Operador and
edad = 20
tiene_licencia = True
puede_conducir = (edad >= 18) and tiene_licencia
print("=== 6.1 Operador AND ===")
print(f"¿Puede conducir? (Edad >= 18 AND Licencia): {puede_conducir}\n")

# Ej 6.2: Operador or
es_fin_de_semana = False
es_feriado = True
hay_descanso = es_fin_de_semana or es_feriado
print("=== 6.2 Operador OR ===")
print(f"¿Hay descanso? (Fin de semana OR Feriado): {hay_descanso}\n")

# Ej 6.3: Operador not
sistema_bloqueado = False
permiso_acceso = not sistema_bloqueado
print("=== 6.3 Operador NOT ===")
print(f"Estado de bloqueo: {sistema_bloqueado}")
print(f"¿Acceso permitido? (NOT sistema_bloqueado): {permiso_acceso}")

print("Hugo Fabian NC = 0040")
