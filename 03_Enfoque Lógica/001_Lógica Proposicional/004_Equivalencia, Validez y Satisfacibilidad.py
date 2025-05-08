from itertools import product

# Equivalencia entre (p ∧ q) ↔ ¬(¬p ∨ ¬q) (Ley de De Morgan)
def verificar_equivalencia():
    print("p\tq\t(p ∧ q)\t¬(¬p ∨ ¬q)\t¿Equivalentes?")  # Imprimimos el encabezado de la tabla
    for p, q in product([True, False], repeat=2):  # Para cada combinación de valores de verdad de p y q
        izquierda = p and q  # Calculamos la conjunción lógica
        derecha = not (not p or not q)  # Calculamos la negación de la disyunción de negaciones
        print(f"{p}\t{q}\t{izquierda}\t{derecha}\t{izquierda == derecha}")  # Imprimimos los valores y la equivalencia

verificar_equivalencia()  # Llamamos a la función para verificar la equivalencia

# Ejemplo de aplicación real: En la lógica proposicional, la equivalencia lógica puede ser utilizada para simplificar expresiones lógicas, considerando las leyes de la lógica como la de De Morgan.
