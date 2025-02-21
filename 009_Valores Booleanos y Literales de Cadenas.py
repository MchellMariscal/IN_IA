# Parte 1: Valores Booleanos
# Aquí uso los valores booleanos True y False
booleano_verdadero = True
booleano_falso = False

# Imprimir los valores booleanos
print("Valor booleano verdadero:", booleano_verdadero)
print("Valor booleano falso:", booleano_falso)

# Haciendo algunas comparaciones y operaciones con booleanos
es_mayor = 10 > 5  # True porque 10 es mayor que 5
es_igual = 10 == 5  # False porque 10 no es igual a 5
es_no_igual = 10 != 5  # True porque 10 es diferente de 5

# Imprimo el resultado de las comparaciones
print("¿Es 10 mayor que 5?", es_mayor)
print("¿Es 10 igual a 5?", es_igual)
print("¿Es 10 diferente de 5?", es_no_igual)

# Parte 2: Literales de Cadenas
# Aquí trabajo con cadenas de texto
cadena_1 = "Hola, soy Michell."
cadena_2 = 'Me gustan los mapaches.'

# Imprimo las cadenas
print("Cadena 1:", cadena_1)
print("Cadena 2:", cadena_2)

# Concatenando las cadenas (uniéndolas)
concatenacion = cadena_1 + " " + cadena_2
print("Cadenas concatenadas:", concatenacion)

# Usando algunos métodos útiles para trabajar con cadenas
longitud = len(cadena_1)  # Me dice cuántos caracteres tiene la cadena
mayusculas = cadena_2.upper()  # Convierte toda la cadena a mayúsculas
minusculas = cadena_1.lower()  # Convierte toda la cadena a minúsculas
reemplazo = cadena_2.replace("Python", "programación")  # Reemplazo "Python" por "programación"

# Imprimo los resultados de los métodos
print("Longitud de la cadena 1:", longitud)
print("Cadena 2 en mayúsculas:", mayusculas)
print("Cadena 1 en minúsculas:", minusculas)
print("Cadena 2 con reemplazo:", reemplazo)

# Parte 3: Comparaciones con cadenas y booleanos
# Comparo si dos cadenas son iguales
cadena_comparacion = "Mapache" == "mapache"  # Esto es False porque Python y python no son iguales (diferentes mayúsculas)
print("¿Es 'Mapache' igual a 'mapache'?", cadena_comparacion)

# Parte 4: Uso de literales booleanos con cadenas
# Comparo si dos cadenas son iguales
es_michell = "Michell" == "Michell"  # Esto es True, porque las cadenas son exactamente iguales
print("¿Es 'Michell' igual a 'Michell'?", es_michell)

# Parte 5: Ejemplo de una decisión con booleanos
edad = 20
mayor_de_edad = edad >= 18  # Aquí evaluamos si la persona es mayor de edad (si la edad es 18 o más)
print("¿Es mayor de edad?", mayor_de_edad)
