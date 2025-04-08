from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Estructura de la red
modelo = BayesianNetwork([('Enfermedad', 'Test')])

# Probabilidad a priori de la enfermedad
cpd_enfermedad = TabularCPD(variable='Enfermedad', variable_card=2, values=[[0.99], [0.01]])

# Probabilidad condicional del test dado enfermedad
cpd_test = TabularCPD(variable='Test', variable_card=2,
                      values=[[0.95, 0.01], [0.05, 0.99]],
                      evidence=['Enfermedad'], evidence_card=[2])

modelo.add_cpds(cpd_enfermedad, cpd_test)

# Inferencia bayesiana
inferencia = VariableElimination(modelo)
resultado = inferencia.query(variables=['Enfermedad'], evidence={'Test': 1})
print(resultado)
