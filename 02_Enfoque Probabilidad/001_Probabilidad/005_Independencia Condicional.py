from pgmpy.models import BayesianNetwork

# Creamos una red bayesiana con tres nodos: Lluvia, Mojado y Paraguas
modelo = BayesianNetwork([
    ('Lluvia', 'Mojado'),  # Lluvia afecta a Mojado
    ('Lluvia', 'Paraguas') # Lluvia afecta a Paraguas
])

# Verificamos la independencia condicional entre Mojado y Paraguas
print(modelo.is_active_trail('Mojado', 'Paraguas'))  # True: Hay un camino activo
print(modelo.is_active_trail('Mojado', 'Paraguas', observed=['Lluvia']))  # False: No hay camino activo dado Lluvia

# Ejemplo de aplicación real: En el análisis de redes sociales, la independencia condicional puede ser utilizada para determinar si dos variables son independientes dado un conjunto de condiciones, como la influencia de un tercer factor.
