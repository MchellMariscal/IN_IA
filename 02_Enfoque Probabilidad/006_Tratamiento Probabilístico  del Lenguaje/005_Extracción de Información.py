import spacy

# Modelo de spaCy (en español)
nlp = spacy.blank('es')

# Texto
texto = "Juan vive en Madrid y trabaja para Google."

# Procesar
doc = nlp(texto)

# Entidades (fingiendo con nombres y ubicaciones)
for token in doc:
    if token.text in ["Juan", "Madrid", "Google"]:
        print(f"Entidad: {token.text}")
