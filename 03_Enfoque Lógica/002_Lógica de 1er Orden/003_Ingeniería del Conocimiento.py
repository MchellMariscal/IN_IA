# Base de hechos y reglas (simple)
hechos = {"EsAnimal": ["Perro", "Gato"]}  # Hechos sobre animales
reglas = {"SiEsAnimal": "TieneCélulas"}  # Reglas sobre animales

def consultar_base(hecho):
    for categoria, elementos in hechos.items():  # Para cada categoría de hechos
        if hecho in elementos:  # Si el hecho está en la categoría
            return reglas.get(f"Si{categoria}", "No se encontró conocimiento.")  # Devolvemos la regla asociada
    return "Hecho desconocido."  # Si el hecho no está en la base

print(consultar_base("Perro"))  # Imprimimos el resultado de la consulta

# Ejemplo de aplicación real: En los sistemas de inteligencia artificial, la ingeniería del conocimiento puede ser utilizada para almacenar y consultar hechos y reglas, permitiendo la inferencia de nueva información.
