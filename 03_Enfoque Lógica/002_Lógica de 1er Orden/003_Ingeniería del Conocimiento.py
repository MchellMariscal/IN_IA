# Base de hechos y reglas (simple)
hechos = {"EsAnimal": ["Perro", "Gato"]}
reglas = {"SiEsAnimal": "TieneCélulas"}

def consultar_base(hecho):
    for categoria, elementos in hechos.items():
        if hecho in elementos:
            return reglas.get(f"Si{categoria}", "No se encontró conocimiento.")
    return "Hecho desconocido."

print(consultar_base("Perro"))
