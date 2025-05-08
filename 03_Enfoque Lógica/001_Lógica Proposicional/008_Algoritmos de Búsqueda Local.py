import random

# Búsqueda local para encontrar una solución que satisfaga (p ∧ q)
def objetivo(p, q):
    return p and q  # Función objetivo: p ∧ q

def busqueda_local():
    mejor_estado = (random.choice([True, False]), random.choice([True, False]))  # Estado inicial aleatorio
    mejor_valor = objetivo(*mejor_estado)  # Valor del estado inicial

    for _ in range(100):  # Para cada iteración
        nuevo_estado = (random.choice([True, False]), random.choice([True, False]))  # Generamos un nuevo estado aleatorio
        nuevo_valor = objetivo(*nuevo_estado)  # Calculamos el valor del nuevo estado
        if nuevo_valor:  # Si el nuevo estado satisface la función objetivo
            return nuevo_estado  # Devolvemos el nuevo estado
    return mejor_estado  # Si no encontramos una solución, devolvemos el mejor estado

solucion = busqueda_local()  # Aplicamos la búsqueda local
print("Solución encontrada (p, q):", solucion)  # Imprimimos la solución encontrada

# Ejemplo de aplicación real: En la optimización, los algoritmos de búsqueda local pueden ser utilizados para encontrar soluciones que satisfagan condiciones lógicas, considerando la exploración del espacio de búsqueda.
