# Simulación de hecho y regla tipo Prolog
def prolog_simulado(base_hechos, regla):
    if regla["if"] in base_hechos:
        return regla["then"]
    return None

base_hechos = {"llueve"}
regla = {"if": "llueve", "then": "llevar_paraguas"}

resultado = prolog_simulado(base_hechos, regla)
print("Consecuencia inferida:", resultado)
