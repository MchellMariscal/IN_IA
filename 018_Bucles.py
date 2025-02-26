# 3.2.1 Bucle while básico
i = 1
while i <= 5:
    print(f"Iteración {i}")
    i += 1

# 3.2.2 Bucle infinito (comentado para evitar problemas)
# while True:
#     print("Este es un bucle infinito")

# 3.2.3 Ejemplo del bucle while
contador = 10
while contador > 0:
    print(f"Cuenta regresiva: {contador}")
    contador -= 1
print("Despegue!")

# 3.2.4 LAB - Adivina el número secreto
numero_secreto = 7
while True:
    intento = int(input("Adivina el número secreto (entre 1 y 10): "))
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        break
    else:
        print("Intenta de nuevo.")

# 3.2.5 Uso del bucle for
for i in range(5):
    print(f"Iteración {i+1} con for")

# 3.2.6 Uso de range con tres argumentos
for i in range(0, 10, 2):
    print(f"Valor actual: {i}")

# 3.2.7 LAB - Contando lentamente
import time
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)  # Pausa de un segundo
print("Tiempo agotado!")

# 3.2.8 Uso de break y continue
for i in range(10):
    if i == 5:
        print("Se detiene en 5")
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Número impar: {i}")

# 3.2.9 LAB - Uso de break atrapado en un bucle
while True:
    palabra = input("Escribe 'salir' para terminar: ")
    if palabra.lower() == "salir":
        break

# 3.2.10 LAB - Uso de continue (el Feo Devorador de Vocales)
frase = input("Ingresa una frase: ")
resultado = ""
for letra in frase:
    if letra.lower() in "aeiou":
        continue
    resultado += letra
print(f"Frase sin vocales: {resultado}")

# 3.2.11 LAB - Uso de continue (el Lindo Devorador de Vocales)
frase = input("Ingresa una frase: ")
resultado = ""
for letra in frase:
    if letra.lower() in "aeiou":
        resultado += letra.upper()
    else:
        resultado += letra
print(f"Frase con vocales en mayúsculas: {resultado}")

# 3.2.12 Bucle while y bloque else
i = 0
while i < 3:
    print(f"Iteración {i}")
    i += 1
else:
    print("El bucle while terminó correctamente")

# 3.2.13 Bucle for y bloque else
for i in range(3):
    print(f"Iteración {i}")
else:
    print("El bucle for terminó correctamente")

# 3.2.14 LAB - Fundamentos de bucles while
numero = 1
while numero <= 5:
    print(f"Número: {numero}")
    numero += 1

# 3.2.15 LAB - La Hipótesis de Collatz
def collatz(n):
    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    print(1)

num = int(input("Ingresa un número para aplicar la Hipótesis de Collatz: "))
collatz(num)

print("Fin de la práctica sobre bucles ")
