import random

def filtrado_particulas(observaciones, transicion, sensor, n=1000):
    particulas = [random.choice(list(transicion.keys())) for _ in range(n)]
    
    for obs in observaciones:
        # Movimiento
        particulas = [random.choices(list(transicion[p].keys()), weights=list(transicion[p].values()))[0] for p in particulas]
        # Pesado
        pesos = [sensor[p].get(obs, 0) for p in particulas]
        # Resampling
        particulas = random.choices(particulas, weights=pesos, k=n)
    
    belief = {estado: particulas.count(estado) / n for estado in transicion}
    return belief

resultado_particulas = filtrado_particulas(observaciones, transicion, sensor)
print("Resultado de filtrado de partículas:")
print(resultado_particulas)
