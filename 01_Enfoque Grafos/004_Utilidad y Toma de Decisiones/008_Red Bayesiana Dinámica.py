from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference

# Crear el modelo
modelo = DBN()

# Definimos la estructura temporal: X_t → O_t y X_t → X_t+1
modelo.add_edges_from([(('X', 0), ('O', 0)), (('X', 0), ('X', 1))])

# CPD inicial de X0
cpd_x0 = TabularCPD(('X', 0), 2, [[0.6], [0.4]])  # P(X0): 0 = soleado, 1 = lluvioso

# CPD de O0 dado X0
cpd_o0 = TabularCPD(('O', 0), 2, [[0.8, 0.3],  # P(O=0|X)
                                  [0.2, 0.7]],  # P(O=1|X)
                    evidence=[('X', 0)], evidence_card=[2])

# CPD de X1 dado X0
cpd_x1 = TabularCPD(('X', 1), 2, [[0.7, 0.4],  # P(X=0|X0)
                                  [0.3, 0.6]],  # P(X=1|X0)
                    evidence=[('X', 0)], evidence_card=[2])

# Añadir CPDs al modelo
modelo.add_cpds(cpd_x0, cpd_o0, cpd_x1)

# Hacer inferencia
infer = DBNInference(modelo)

# Consulta: ¿cuál es la probabilidad del estado en t=1 si observamos O0 = lluvioso (1)?
query = infer.query(variables=[('X', 1)], evidence={('O', 0): 1})
print("Inferencia: P(X1 | O0 = lluvioso):")
print(query)
