# Parte 1: Python como una calculadora
# Aquí vamos a hacer algunas operaciones básicas

# Suma
suma = 8 + 5
print("Suma de 8 + 5:", suma)

# Resta
resta = 10 - 4
print("Resta de 10 - 4:", resta)

# Multiplicación
multiplicacion = 7 * 6
print("Multiplicación de 7 * 6:", multiplicacion)

# División
division = 20 / 4
print("División de 20 / 4:", division)

# División entera (cuando solo quiero el número entero sin decimales)
division_entera = 20 // 3
print("División entera de 20 // 3:", division_entera)

# Módulo (resto de la división)
modulo = 20 % 3
print("Módulo de 20 % 3:", modulo)

# Potencia (es como hacer exponente)
potencia = 2 ** 3
print("Potencia de 2 ** 3:", potencia)

# Parte 2: Operadores Básicos
# Usamos dos números, a y b, para practicar con operaciones
a = 15
b = 4

# Suma
resultado_suma = a + b
# Resta
resultado_resta = a - b
# Multiplicación
resultado_multiplicacion = a * b
# División
resultado_division = a / b
# Potencia
resultado_potencia = a ** b
# Módulo
resultado_modulo = a % b

# Imprimir los resultados
print("\nResultados prácticos:")
print(f"{a} + {b} = {resultado_suma}")
print(f"{a} - {b} = {resultado_resta}")
print(f"{a} * {b} = {resultado_multiplicacion}")
print(f"{a} / {b} = {resultado_division}")
print(f"{a} ** {b} = {resultado_potencia}")
print(f"{a} % {b} = {resultado_modulo}")

# Parte 3: Operadores y sus prioridades
# En Python, las multiplicaciones y divisiones tienen más prioridad que sumas y restas

# Aquí, Python va a hacer primero la multiplicación
resultado_prioridad = 2 + 3 * 4  # Primero hace 3 * 4 y después suma 2
print("\nResultado con prioridades de operadores (2 + 3 * 4):", resultado_prioridad)

# Si quiero cambiar el orden de las operaciones, uso paréntesis
resultado_con_parentesis = (2 + 3) * 4  # Primero hace 2 + 3 y después multiplica por 4
print("Resultado con paréntesis (2 + 3) * 4:", resultado_con_parentesis)

# Otra operación con diferentes operadores
resultado_complejo = (5 + 3) * 2 ** 3 / 4  # Python hace la potencia antes que la multiplicación y división
print("Resultado de (5 + 3) * 2 ** 3 / 4:", resultado_complejo)

# Operadores lógicos: Estos me sirven para hacer comparaciones (True/False)
# Por ejemplo, AND, OR, NOT
condicion1 = True
condicion2 = False
and_result = condicion1 and condicion2  # AND, sólo es True si ambos son True
or_result = condicion1 or condicion2  # OR, es True si al menos uno es True
not_result = not condicion1  # NOT, invierte el valor de True a False

print("\nOperadores lógicos:")
print(f"condicion1 and condicion2: {and_result}")
print(f"condicion1 or condicion2: {or_result}")
print(f"not condicion1: {not_result}")
