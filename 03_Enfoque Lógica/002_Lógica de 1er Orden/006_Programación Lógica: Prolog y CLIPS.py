# Simulación de hecho y regla tipo Prolog
def prolog_simulado(base_hechos, regla):
    if regla["if"] in base_hechos:  # Si el antecedente de la regla es un hecho conocido
        return regla["then"]  # Devolvemos el consecuente de la regla
    return None  # No se puede inferir el consecuente

base_hechos = {"llueve"}  # Hechos conocidos
regla = {"if": "llueve", "then": "llevar_paraguas"}  # Regla de inferencia

resultado = prolog_simulado(base_hechos, regla)  # Aplicamos la simulación de Prolog
print("Consecuencia inferida:", resultado)  # Imprimimos el resultado de la inferencia

# Ejemplo de aplicación real: En la programación lógica, Prolog y CLIPS pueden ser utilizados para implementar sistemas de inferencia basados en reglas, considerando los hechos y reglas para realizar inferencias.
