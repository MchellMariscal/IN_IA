# Ejemplo 1: Uso básico de input()
print("Hola! Escribe algo y te responderé: ")
respuesta = input()
print("Wow!", respuesta, "suena interesante.")

# Ejemplo 2: Usando input() con un mensaje
respuesta = input("Dime algo curioso: ")
print("No lo sabía...", respuesta, "¡qué interesante!")

# Ejemplo 3: Problema con tipos de datos
numero = input("Escribe un número: ")
# Intentar hacer operaciones sin convertirlo generará un error
# resultado = numero ** 2  # Esto da un TypeError

# Ejemplo 4: Solucionando con conversión de tipos
numero_entero = int(input("Escribe un número entero: "))
print("El cuadrado de tu número es:", numero_entero ** 2)

numero_flotante = float(input("Ahora escribe un número con decimales: "))
print("El cuadrado de ese número es:", numero_flotante ** 2)
