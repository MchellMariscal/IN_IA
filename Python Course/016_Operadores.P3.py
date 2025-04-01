# Igualdad (==) y desigualdad (!=)
print("¿2 es igual a 2?", 2 == 2)
print("¿2 es igual a 2.0?", 2 == 2.0)
print("¿1 es igual a 2?", 1 == 2)
print("¿5 no es igual a 3?", 5 != 3)
print("¿10 no es igual a 10?", 10 != 10)

# Comparaciones mayores y menores
print("¿5 es mayor que 3?", 5 > 3)
print("¿2 es mayor que 7?", 2 > 7)
print("¿10 es mayor o igual a 10?", 10 >= 10)
print("¿4 es menor que 6?", 4 < 6)
print("¿7 es menor o igual a 7?", 7 <= 7)

# Comparaciones con variables
black_sheep = int(input("Ingresa la cantidad de ovejas negras: "))
white_sheep = int(input("Ingresa la cantidad de ovejas blancas: "))
print("¿Hay el doble de ovejas negras que blancas?", black_sheep == 2 * white_sheep)

centigrade_outside = float(input("Ingresa la temperatura en grados Celsius: "))
print("¿Es necesario usar gorro?", centigrade_outside <= 0.0)

current_velocity_mph = float(input("Ingresa la velocidad actual en mph: "))
print("¿Riesgo de multa por exceso de velocidad?", current_velocity_mph > 85)
