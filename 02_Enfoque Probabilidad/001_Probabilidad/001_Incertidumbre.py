from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Creamos una red bayesiana simple
modelo = BayesianNetwork([('Lluvia', 'CespedMojado')])

# Definimos las probabilidades
cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2, values=[[0.3], [0.7]])  # 0: no llueve, 1: llueve
cpd_cesped = TabularCPD(variable='CespedMojado', variable_card=2,
                        values=[[0.9, 0.2], [0.1, 0.8]],
                        evidence=['Lluvia'], evidence_card=[2])

modelo.add_cpds(cpd_lluvia, cpd_cesped)

# Inferencia
inferencia = VariableElimination(modelo)
prob = inferencia.query(variables=['Lluvia'], evidence={'CespedMojado': 1})
print(prob)
