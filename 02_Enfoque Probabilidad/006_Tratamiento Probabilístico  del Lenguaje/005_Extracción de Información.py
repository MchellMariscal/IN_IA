import spacy

# Modelo de spaCy en español
nlp = spacy.blank('es')  # Inicializamos el modelo en español

# Texto de ejemplo
texto = "Juan vive en Madrid y trabaja para Google."  # Texto

# Procesar el texto con spaCy
doc = nlp(texto)  # Procesamos el texto

# Entidades (fingiendo con nombres y ubicaciones)
for token in doc:  # Para cada token en el documento
    if token.text in ["Juan", "Madrid", "Google"]:  # Si el token es una entidad
        print(f"Entidad: {token.text}")  # Imprimimos la entidad

# Ejemplo de aplicación real: En el análisis de texto, la extracción de información puede ser utilizada para identificar entidades como nombres, ubicaciones y organizaciones, considerando el contexto del texto.
