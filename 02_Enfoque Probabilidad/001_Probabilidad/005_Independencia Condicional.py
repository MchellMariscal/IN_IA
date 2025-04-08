from pgmpy.models import BayesianNetwork

# Estructura: Lluvia → Mojado, Lluvia → Paraguas
modelo = BayesianNetwork([
    ('Lluvia', 'Mojado'),
    ('Lluvia', 'Paraguas')
])

# Verificamos independencia condicional
print(modelo.is_active_trail('Mojado', 'Paraguas'))  # True
print(modelo.is_active_trail('Mojado', 'Paraguas', observed=['Lluvia']))  # False
