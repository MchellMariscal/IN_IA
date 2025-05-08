import numpy as np

# Configuración de la cuadrícula 3x3
filas, columnas = 3, 3
estados = [(i, j) for i in range(filas) for j in range(columnas)]  # Todos los estados
acciones = ['arriba', 'abajo', 'izquierda', 'derecha']  # Acciones posibles
gamma = 0.9  # Factor de descuento
theta = 0.001  # Umbral de convergencia
meta = (2, 2)  # Estado objetivo con recompensa alta

# Recompensas por estado
def recompensa(estado):
    if estado == meta:  # Si es el estado meta
        return 10  # Recompensa alta
    else:
        return -1  # Penalización por movimiento

# Transiciones determinísticas
def mover(estado, accion):
    i, j = estado  # Posición actual
    if accion == 'arriba':  # Mover arriba
        i = max(i - 1, 0)  # Nueva posición
    elif accion == 'abajo':  # Mover abajo
        i = min(i + 1, filas - 1)  # Nueva posición
    elif accion == 'izquierda':  # Mover izquierda
        j = max(j - 1, 0)  # Nueva posición
    elif accion == 'derecha':  # Mover derecha
        j = min(j + 1, columnas - 1)  # Nueva posición
    return (i, j)  # Devolvemos la nueva posición

# Inicializar valores y política
V = {s: 0 for s in estados}  # Valores iniciales para cada estado
politica = {s: acciones[0] for s in estados}  # Política inicial

# Iteración de valores
while True:
    delta = 0  # Cambio máximo en los valores
    for s in estados:  # Para cada estado
        if s == meta:  # Si es el estado meta
            continue  # Saltamos a la siguiente iteración
        v = V[s]  # Valor actual del estado
        valores_accion = []  # Valores para cada acción
        for a in acciones:  # Para cada acción
            siguiente = mover(s, a)  # Nueva posición
            r = recompensa(siguiente)  # Recompensa
            valores_accion.append(r + gamma * V[siguiente])  # Valor de la acción
        V[s] = max(valores_accion)  # Actualizamos el valor del estado
        delta = max(delta, abs(v - V[s]))  # Actualizamos el cambio máximo
    if delta < theta:  # Si el cambio es menor que el umbral
        break  # Terminamos las iteraciones

# Derivar la política óptima
for s in estados:  # Para cada estado
    if s == meta:  # Si es el estado meta
        politica[s] = 'META'  # Acción meta
        continue  # Saltamos a la siguiente iteración
    mejor_valor = float('-inf')  # Mejor valor
    mejor_accion = None  # Mejor acción
    for a in acciones:  # Para cada acción
        siguiente = mover(s, a)  # Nueva posición
        r = recompensa(siguiente)  # Recompensa
        valor = r + gamma * V[siguiente]  # Valor de la acción
        if valor > mejor_valor:  # Si el valor es mejor
            mejor_valor = valor  # Actualizamos el mejor valor
            mejor_accion = a  # Actualizamos la mejor acción
    politica[s] = mejor_accion  # Actualizamos la política

# Mostrar la política
print("Política óptima:")  # Imprimimos la política óptima
for i in range(filas):  # Para cada fila
    fila = ''  # Cadena para la fila
    for j in range(columnas):  # Para cada columna
        fila += f"{politica[(i, j)]:^10}"  # Añadimos la acción
    print(fila)  # Imprimimos la fila

# Mostrar valores
print("\nValores por estado:")  # Imprimimos los valores por estado
for i in range(filas):  # Para cada fila
    fila = ''  # Cadena para la fila
    for j in range(columnas):  # Para cada columna
        fila += f"{V[(i, j)]:^10.2f}"  # Añadimos el valor
    print(fila)  # Imprimimos la fila

# Ejemplo de aplicación real: En la navegación autónoma, los procesos de decisión de Markov pueden ser utilizados para determinar la mejor ruta que un vehículo autónomo debe seguir, considerando las recompensas y penalizaciones asociadas a diferentes acciones.
