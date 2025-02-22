# Expresión matemática compleja
print("Vamos a evaluar una expresión matemática!")
x = float(input("Ingresa un valor para x: "))
y = 1 / (x + (1 / (x + (1 / (x + (1 / x))))))  # Expresión con operadores
print("El resultado de la expresión es:", y)

# Otra expresión con operadores básicos
print("Vamos a realizar otra operación con operadores.")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
resultado = (a + b) * (a - b) / (a * b)
print("El resultado de la operación es:", resultado)

# Uso de paréntesis para priorizar operaciones
print("Evaluando una expresión con prioridad de operadores.")
c = float(input("Ingresa un número para evaluar: "))
expresion = ((c + 2) ** 2) / ((c - 1) + 3)
print("El resultado de la expresión es:", expresion)
