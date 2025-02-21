# Sección 5 – Comentarios

# Los comentarios son muy importantes porque ayudan a que el código sea más fácil de entender.
# Python ignora todo lo que está después de un "#", así que podemos escribir lo que queramos ahí.

# Parte 1: Comentarios de una sola línea
# En esta parte, asigno valores a mis variables, pero también voy a poner comentarios para explicar lo que hago.

nombre = "Michell"  # Mi nombre
edad = 20  # Mi edad
altura = 1.62  # Mi altura

# Parte 2: Comentarios multilínea
"""
Este es un comentario de varias líneas.
Aquí puedo escribir algo largo para explicar lo que hace mi código.
Es útil cuando el comentario necesita más espacio.
"""

# Parte 3: Imprimiendo el valor de las variables
print("Mi nombre es:", nombre)  # Aquí imprimo el nombre
print("Mi edad es:", edad)  # Aquí imprimo la edad
print("Mi altura es:", altura)  # Aquí imprimo la altura

# Parte 4: Comentarios dentro de funciones
def saludo():
    # Esta es una función que imprime un saludo personalizado con mi nombre y edad.
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# Llamando la función saludo
saludo()

# Parte 5: Comentarios al final de la línea
resultado = edad * altura  # Multiplico la edad por la altura

# Imprimiendo el resultado
print("El resultado de multiplicar edad por altura es:", resultado)

# Comentario final explicando el uso de los comentarios
# Los comentarios hacen que el código sea más fácil de entender.
# Así, si alguien más lee el código (o yo mismo después de un tiempo),
# puede saber exactamente lo que está pasando sin tener que descifrar cada línea.
