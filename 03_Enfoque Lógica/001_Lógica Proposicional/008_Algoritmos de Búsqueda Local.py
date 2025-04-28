import random

# Búsqueda local para encontrar una solución que satisfaga (p ∧ q)
def objetivo(p, q):
    return p and q

def busqueda_local():
    mejor_estado = (random.choice([True, False]), random.choice([True, False]))
    mejor_valor = objetivo(*mejor_estado)

    for _ in range(100):
        nuevo_estado = (random.choice([True, False]), random.choice([True, False]))
        nuevo_valor = objetivo(*nuevo_estado)
        if nuevo_valor:
            return nuevo_estado
    return mejor_estado

solucion = busqueda_local()
print("Solución encontrada (p, q):", solucion)
