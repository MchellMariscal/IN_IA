# Igualdad (==) y desigualdad (!=)
print("¿2 es igual a 2? (Debería ser True)", 2 == 2)
print("¿2 es igual a 2.0? (Debería ser True)", 2 == 2.0)
print("¿1 es igual a 2? (Debería ser False)", 1 == 2)
print("¿5 no es igual a 3? (Debería ser True)", 5 != 3)
print("¿10 no es igual a 10? (Debería ser False)", 10 != 10)

# Comparaciones mayores y menores
print("¿5 es mayor que 3? (Debería ser True)", 5 > 3)
print("¿2 es mayor que 7? (Debería ser False)", 2 > 7)
print("¿10 es mayor o igual a 10? (Debería ser True)", 10 >= 10)
print("¿4 es menor que 6? (Debería ser True)", 4 < 6)
print("¿7 es menor o igual a 7? (Debería ser True)", 7 <= 7)

# Comparaciones con cadenas
print("¿'Hola' es igual a 'hola'? (Debería ser False)", "Hola" == "hola")
print("¿'Python' es mayor que 'Java'? (Comparación lexicográfica)", "Python" > "Java")

# Comparaciones con booleanos
print("¿True es igual a 1? (Debería ser True)", True == 1)
print("¿False es menor que True? (Debería ser True)", False < True)

# Comparaciones con variables
gatos = int(input("Ingresa la cantidad de gatos: "))
perros = int(input("Ingresa la cantidad de perros: "))
print(f"Tienes {gatos} gatos y {perros} perros.")
print("¿Tienes más gatos que perros?", gatos > perros)

black_sheep = int(input("Ingresa la cantidad de ovejas negras en el rebaño: "))
white_sheep = int(input("Ingresa la cantidad de ovejas blancas en el rebaño: "))
print(f"Hay {black_sheep} ovejas negras y {white_sheep} ovejas blancas.")
print("¿Hay el doble de ovejas negras que blancas?", black_sheep == 2 * white_sheep)

centigrade_outside = float(input("Ingresa la temperatura en grados Celsius: "))
if centigrade_outside <= 0.0:
    print("¡Hace frío! Ponte gorro.")
else:
    print("No necesitas gorro, pero abrígate si hace frío.")

current_velocity_mph = float(input("Ingresa la velocidad actual en mph: "))
print("¿Riesgo de multa por exceso de velocidad?", current_velocity_mph > 85)

# 3.1.11 LAB - Calculadora de impuestos
ingreso = float(input("Ingresa tu ingreso anual: "))
if ingreso <= 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = 14839.02 + (ingreso - 85528) * 0.32
impuesto = max(0, round(impuesto))
print(f"El impuesto es: {impuesto} pesos")

# 3.1.12 LAB - Determinar si un año es bisiesto
año = int(input("Ingresa un año: "))
if año < 1582:
    print("No dentro del período del calendario Gregoriano")
elif año % 4 != 0:
    print("Año común")
elif año % 100 != 0:
    print("Año bisiesto")
elif año % 400 != 0:
    print("Año común")
else:
    print("Año bisiesto")

# 3.1.13 Resumen - Ejemplos de estructuras if, if-else, if-elif-else
x = 10
if x == 10:
    print("x == 10")
if x > 15:
    print("x > 15")
elif x > 10:
    print("x > 10")
elif x > 5:
    print("x > 5")
else:
    print("else no será ejecutado")
