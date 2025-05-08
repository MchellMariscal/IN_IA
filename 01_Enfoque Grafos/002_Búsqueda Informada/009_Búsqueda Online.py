import random

# Representación del laberinto
laberinto = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'G'],
    'F': ['D'],
    'G': ['E']
}

# Función de búsqueda online
def busqueda_online(laberinto, inicio, objetivo):
    estado_actual = inicio
    visitados = set()
    camino = [estado_actual]

    while estado_actual != objetivo:
        visitados.add(estado_actual)

        # Obtenemos vecinos no visitados
        vecinos = [n for n in laberinto.get(estado_actual, []) if n not in visitados]

        if vecinos:
            estado_actual = random.choice(vecinos)  # Elegimos un vecino aleatorio
        else:
            if len(camino) > 1:
                camino.pop()  # Retrocedemos si no hay opciones
                estado_actual = camino[-1]
            else:
                return None  # No hay solución

        camino.append(estado_actual)

    return camino

# Ejecutamos la búsqueda online desde 'A' hasta 'G'
resultado = busqueda_online(laberinto, 'A', 'G')
print(f'Ruta encontrada con Búsqueda Online: {resultado}')

# Ejemplo de aplicación real: En la exploración de entornos desconocidos por robots, la búsqueda online puede ser utilizada para encontrar rutas seguras y eficientes, adaptándose a cambios en el entorno en tiempo real.
