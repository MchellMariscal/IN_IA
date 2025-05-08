import random

# Función para el filtrado de partículas
def filtrado_particulas(observaciones, transicion, sensor, n=1000):
    particulas = [random.choice(list(transicion.keys())) for _ in range(n)]  # Inicializamos las partículas

    for obs in observaciones:  # Para cada observación
        # Movimiento
        particulas = [random.choices(list(transicion[p].keys()), weights=list(transicion[p].values()))[0] for p in particulas]  # Movemos las partículas
        # Pesado
        pesos = [sensor[p].get(obs, 0) for p in particulas]  # Calculamos los pesos
        # Re-muestreo
        particulas = random.choices(particulas, weights=pesos, k=n)  # Re-muestreamos

    belief = {estado: particulas.count(estado) / n for estado in transicion}  # Calculamos la creencia
    return belief  # Devolvemos la creencia

resultado_particulas = filtrado_particulas(observaciones, transicion, sensor)  # Realizamos el filtrado
print("Resultado de filtrado de partículas:")  # Imprimimos el resultado
print(resultado_particulas)  # Imprimimos la creencia

# Ejemplo de aplicación real: En la robótica, el filtrado de partículas puede ser utilizado para estimar la posición de un robot en un entorno, considerando las observaciones ruidosas y las transiciones entre estados.
