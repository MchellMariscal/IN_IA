from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Creamos una red bayesiana con dos nodos: Enfermedad y Test
modelo = BayesianNetwork([('Enfermedad', 'Test')])

# Definimos las probabilidades a priori para el nodo Enfermedad
# 0: no tiene la enfermedad, 1: tiene la enfermedad
cpd_enfermedad = TabularCPD(variable='Enfermedad', variable_card=2, values=[[0.99], [0.01]])

# Definimos las probabilidades condicionales para el nodo Test dado Enfermedad
# [P(Test=0|Enfermedad), P(Test=1|Enfermedad)]
cpd_test = TabularCPD(variable='Test', variable_card=2,
                      values=[[0.95, 0.01], [0.05, 0.99]],
                      evidence=['Enfermedad'], evidence_card=[2])

# Añadimos las CPDs al modelo
modelo.add_cpds(cpd_enfermedad, cpd_test)

# Realizamos inferencia bayesiana
inferencia = VariableElimination(modelo)
# Calculamos la probabilidad de tener la enfermedad dado un test positivo
resultado = inferencia.query(variables=['Enfermedad'], evidence={'Test': 1})
print(resultado)  # Imprimimos el resultado de la inferencia

# Ejemplo de aplicación real: En la medicina, la probabilidad a priori puede ser utilizada para evaluar la probabilidad de que un paciente tenga una enfermedad antes de realizar pruebas diagnósticas, basándose en datos históricos.
