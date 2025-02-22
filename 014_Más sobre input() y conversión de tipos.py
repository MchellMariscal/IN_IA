import math  # Importamos la librería para usar funciones matemáticas

# Ejemplo 1: Calculando la hipotenusa de un triángulo rectángulo
print("Vamos a calcular la hipotenusa de un triángulo rectángulo!")
a = float(input("Introduce el valor del primer cateto: "))
b = float(input("Introduce el valor del segundo cateto: "))
hipotenusa = math.sqrt(a**2 + b**2)
print("La hipotenusa es:", hipotenusa)

# Ejemplo 2: Uso de concatenación con +
nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
print("Hola " + nombre + ", tienes " + edad + " años.")

# Ejemplo 3: Uso del operador * con cadenas
caracter = input("Elige un caracter para dibujar una línea: ")
repeticiones = int(input("¿Cuántas veces quieres repetirlo? "))
print(caracter * repeticiones)

# Ejemplo 4: Conversión de tipos con str()
num = 5
mensaje = "El número es " + str(num)
print(mensaje)
