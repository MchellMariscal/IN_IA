from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura del grafo
modelo = BayesianNetwork([
    ('Lluvia', 'Pasto'),
    ('Rociador', 'Pasto')
])

# Tablas de probabilidad condicional
cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2, values=[[0.7], [0.3]])  # 0: No, 1: Sí
cpd_rociador = TabularCPD(variable='Rociador', variable_card=2, values=[[0.6], [0.4]])

cpd_pasto = TabularCPD(
    variable='Pasto',
    variable_card=2,
    evidence=['Lluvia', 'Rociador'],
    evidence_card=[2, 2],
    values=[
        [1.0, 0.1, 0.1, 0.01],  # Pasto seco
        [0.0, 0.9, 0.9, 0.99]   # Pasto mojado
    ]
)

# Asociamos las tablas al modelo
modelo.add_cpds(cpd_lluvia, cpd_rociador, cpd_pasto)

# Inferencia: ¿Cuál es la probabilidad de que haya llovido si el pasto está mojado?
infer = VariableElimination(modelo)
resultado = infer.query(variables=['Lluvia'], evidence={'Pasto': 1})

print(resultado)
