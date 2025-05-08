import random

# Función para muestrear si está nublado
def sample_cloudy():
    return random.random() < 0.5  # Probabilidad de que esté nublado

# Función para muestrear si el rociador está encendido dado si está nublado
def sample_sprinkler(cloudy):
    if cloudy:  # Si está nublado
        return random.random() < 0.1  # Probabilidad de que el rociador esté encendido
    else:  # Si no está nublado
        return random.random() < 0.5  # Probabilidad de que el rociador esté encendido

# Función para la probabilidad de que el pasto esté mojado dado el rociador
def wetgrass_prob(sprinkler):
    return 0.9 if sprinkler else 0.2  # Probabilidad de que el pasto esté mojado

# Función para la ponderación de verosimilitud
def likelihood_weighting(n_samples=10000, evidence={'WetGrass': True}):
    weighted_samples = []  # Lista para guardar las muestras ponderadas

    for _ in range(n_samples):  # Para cada muestra
        sample = {}  # Diccionario para la muestra
        weight = 1.0  # Peso inicial

        # 1. Muestrear si está nublado
        cloudy = sample_cloudy()  # Muestreo de Cloudy
        sample['Cloudy'] = cloudy  # Guardamos el valor

        # 2. Muestrear si el rociador está encendido dado si está nublado
        sprinkler = sample_sprinkler(cloudy)  # Muestreo de Sprinkler
        sample['Sprinkler'] = sprinkler  # Guardamos el valor

        # 3. No muestrear WetGrass, solo ponderar
        wet_prob = wetgrass_prob(sprinkler)  # Probabilidad de WetGrass
        weight *= wet_prob if evidence['WetGrass'] else (1 - wet_prob)  # Ponderamos

        weighted_samples.append((sample, weight))  # Guardamos la muestra ponderada

    # 4. Estimar P(Cloudy=True | WetGrass=True)
    cloudy_true = sum(weight for (s, weight) in weighted_samples if s['Cloudy'])  # Suma de pesos para Cloudy=True
    total_weight = sum(weight for (_, weight) in weighted_samples)  # Suma total de pesos

    return cloudy_true / total_weight  # Devolvemos la probabilidad estimada

# Ejecutar
resultado = likelihood_weighting()  # Calculamos P(Cloudy=True | WetGrass=True)
print(f"P(Cloudy=True | WetGrass=True) ≈ {resultado:.4f}")  # Imprimimos el resultado

# Ejemplo de aplicación real: En el análisis de riesgos, la ponderación de verosimilitud puede ser utilizada para estimar la probabilidad de eventos raros, considerando la evidencia disponible y ajustando las estimaciones en consecuencia.
