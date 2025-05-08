import random

# Función objetivo (aptitud) a maximizar: f(x) = x^2
def fitness(x):
    return x ** 2

# Generar población inicial de n individuos (valores enteros entre -10 y 10)
def generar_poblacion(n):
    return [random.randint(-10, 10) for _ in range(n)]

# Selección por torneo: elige los 2 mejores de un grupo aleatorio
def seleccion(poblacion):
    torneo = random.sample(poblacion, 3)
    torneo.sort(key=fitness, reverse=True)
    return torneo[0], torneo[1]

# Cruce de 2 padres: promedia sus valores
def cruce(padre1, padre2):
    return (padre1 + padre2) // 2  # Cruce simple

# Mutación: cambia un valor con pequeña probabilidad
def mutacion(individuo):
    if random.random() < 0.2:  # 20% de probabilidad de mutación
        return individuo + random.randint(-1, 1)
    return individuo

# Algoritmo Genético principal
def algoritmo_genetico(tamaño_poblacion, generaciones):
    poblacion = generar_poblacion(tamaño_poblacion)

    for _ in range(generaciones):
        nueva_poblacion = []

        for _ in range(tamaño_poblacion // 2):  # Se generan parejas
            padre1, padre2 = seleccion(poblacion)
            hijo = cruce(padre1, padre2)
            hijo = mutacion(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    # Devolver el mejor individuo encontrado
    return max(poblacion, key=fitness)

# Ejecutar el Algoritmo Genético
mejor_solucion = algoritmo_genetico(tamaño_poblacion=10, generaciones=20)
print(f'Mejor solución encontrada: {mejor_solucion}, con fitness: {fitness(mejor_solucion)}')

# Ejemplo de aplicación real: En la optimización de diseños de ingeniería, los algoritmos genéticos pueden ser utilizados para encontrar la configuración de diseño que maximiza el rendimiento y minimiza los costos de producción.
