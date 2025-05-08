from itertools import product

# Definir una función para tabla de verdad de p → q
def tabla_verdad():
    print("p\tq\tp → q")  # Imprimimos el encabezado de la tabla
    for p, q in product([True, False], repeat=2):  # Para cada combinación de valores de verdad de p y q
        implicacion = (not p) or q  # Calculamos la implicación lógica
        print(f"{p}\t{q}\t{implicacion}")  # Imprimimos los valores de p, q y la implicación

tabla_verdad()  # Llamamos a la función para generar la tabla de verdad

# Ejemplo de aplicación real: En la lógica proposicional, las tablas de verdad pueden ser utilizadas para evaluar la validez de proposiciones lógicas, considerando todas las posibles combinaciones de valores de verdad.
