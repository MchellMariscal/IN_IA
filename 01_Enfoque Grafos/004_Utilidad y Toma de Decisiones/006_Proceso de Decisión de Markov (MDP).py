import numpy as np

# Configuración de la cuadrícula 3x3
filas, columnas = 3, 3
estados = [(i, j) for i in range(filas) for j in range(columnas)]
acciones = ['arriba', 'abajo', 'izquierda', 'derecha']
gamma = 0.9
theta = 0.001  # Umbral de convergencia
meta = (2, 2)  # Estado objetivo con recompensa alta

# Recompensas por estado
def recompensa(estado):
    if estado == meta:
        return 10
    else:
        return -1  # Penalización por movimiento

# Transiciones determinísticas
def mover(estado, accion):
    i, j = estado
    if accion == 'arriba':
        i = max(i - 1, 0)
    elif accion == 'abajo':
        i = min(i + 1, filas - 1)
    elif accion == 'izquierda':
        j = max(j - 1, 0)
    elif accion == 'derecha':
        j = min(j + 1, columnas - 1)
    return (i, j)

# Inicializar valores y política
V = {s: 0 for s in estados}
politica = {s: acciones[0] for s in estados}

# Iteración de valores
while True:
    delta = 0
    for s in estados:
        if s == meta:
            continue
        v = V[s]
        valores_accion = []
        for a in acciones:
            siguiente = mover(s, a)
            r = recompensa(siguiente)
            valores_accion.append(r + gamma * V[siguiente])
        V[s] = max(valores_accion)
        delta = max(delta, abs(v - V[s]))
    if delta < theta:
        break

# Derivar la política óptima
for s in estados:
    if s == meta:
        politica[s] = 'META'
        continue
    mejor_valor = float('-inf')
    mejor_accion = None
    for a in acciones:
        siguiente = mover(s, a)
        r = recompensa(siguiente)
        valor = r + gamma * V[siguiente]
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_accion = a
    politica[s] = mejor_accion

# Mostrar la política
print("Política óptima:")
for i in range(filas):
    fila = ''
    for j in range(columnas):
        fila += f"{politica[(i, j)]:^10}"
    print(fila)

# Mostrar valores
print("\nValores por estado:")
for i in range(filas):
    fila = ''
    for j in range(columnas):
        fila += f"{V[(i, j)]:^10.2f}"
    print(fila)
