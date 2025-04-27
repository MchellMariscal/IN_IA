from collections import Counter

datos = [
    {"color": "rojo", "textura": "liso", "etiqueta": "manzana"},
    {"color": "naranja", "textura": "rugoso", "etiqueta": "naranja"},
    {"color": "rojo", "textura": "rugoso", "etiqueta": "manzana"},
]

# Contadores
conteo = Counter((d["color"], d["textura"], d["etiqueta"]) for d in datos)

# Nueva fruta
color = "rojo"
textura = "liso"

# Clasificación
p_manzana = conteo[(color, textura, "manzana")] + 1
p_naranja = conteo[(color, textura, "naranja")] + 1

print("Manzana" if p_manzana > p_naranja else "Naranja")
