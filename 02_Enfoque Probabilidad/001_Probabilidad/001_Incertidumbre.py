from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Creamos una red bayesiana simple con dos nodos: Lluvia y CespedMojado
modelo = BayesianNetwork([('Lluvia', 'CespedMojado')])

# Definimos las probabilidades a priori para el nodo Lluvia
# 0: no llueve, 1: llueve
cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2, values=[[0.3], [0.7]])

# Definimos las probabilidades condicionales para el nodo CespedMojado dado Lluvia
# [P(CespedMojado=0|Lluvia), P(CespedMojado=1|Lluvia)]
cpd_cesped = TabularCPD(variable='CespedMojado', variable_card=2,
                        values=[[0.9, 0.2], [0.1, 0.8]],
                        evidence=['Lluvia'], evidence_card=[2])

# Añadimos las CPDs al modelo
modelo.add_cpds(cpd_lluvia, cpd_cesped)

# Realizamos inferencia bayesiana
inferencia = VariableElimination(modelo)
# Calculamos la probabilidad de que llueva dado que el césped está mojado
prob = inferencia.query(variables=['Lluvia'], evidence={'CespedMojado': 1})
print(prob)  # Imprimimos el resultado de la inferencia

# Ejemplo de aplicación real: En la meteorología, las redes bayesianas pueden ser utilizadas para modelar la incertidumbre en las predicciones del clima, considerando diferentes factores como la lluvia y sus efectos.
