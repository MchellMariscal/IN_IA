from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura del grafo de la red bayesiana
modelo = BayesianNetwork([
    ('Lluvia', 'Pasto'),  # Lluvia afecta a Pasto
    ('Rociador', 'Pasto') # Rociador afecta a Pasto
])

# Tablas de probabilidad condicional para cada nodo
# P(Lluvia): 0: No llueve, 1: Llueve
cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2, values=[[0.7], [0.3]])

# P(Rociador): 0: No se usa el rociador, 1: Se usa el rociador
cpd_rociador = TabularCPD(variable='Rociador', variable_card=2, values=[[0.6], [0.4]])

# P(Pasto | Lluvia, Rociador): Pasto seco o mojado dado Lluvia y Rociador
cpd_pasto = TabularCPD(
    variable='Pasto',
    variable_card=2,
    evidence=['Lluvia', 'Rociador'],  # Dependencias
    evidence_card=[2, 2],  # Cardinalidad de las variables de evidencia
    values=[
        [1.0, 0.1, 0.1, 0.01],  # Pasto seco
        [0.0, 0.9, 0.9, 0.99]   # Pasto mojado
    ]
)

# Asociamos las tablas al modelo
modelo.add_cpds(cpd_lluvia, cpd_rociador, cpd_pasto)

# Inferencia: ¿Cuál es la probabilidad de que haya llovido si el pasto está mojado?
infer = VariableElimination(modelo)
resultado = infer.query(variables=['Lluvia'], evidence={'Pasto': 1})  # P(Lluvia | Pasto=1)

print(resultado)  # Imprimimos el resultado de la inferencia

# Ejemplo de aplicación real: En la agricultura, las redes bayesianas pueden ser utilizadas para modelar la probabilidad de que el pasto esté mojado, considerando factores como la lluvia y el uso de rociadores, ayudando a optimizar el riego.
