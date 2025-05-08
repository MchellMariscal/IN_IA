from sklearn.feature_extraction.text import TfidfVectorizer

# Documentos de ejemplo
docs = [
    "el gato duerme en la cama",  # Documento 1
    "el perro corre en el parque",  # Documento 2
    "los gatos y perros son animales"  # Documento 3
]

# Vectorización TF-IDF: convertimos los documentos en vectores TF-IDF
vectorizer = TfidfVectorizer()  # Inicializamos el vectorizador
X = vectorizer.fit_transform(docs)  # Vectorizamos los documentos

# Consulta de ejemplo
query = "gato cama"  # Consulta

query_vec = vectorizer.transform([query])  # Vectorizamos la consulta

# Similaridad coseno: calculamos la similitud entre la consulta y los documentos
from sklearn.metrics.pairwise import cosine_similarity
similaridad = cosine_similarity(query_vec, X)  # Calculamos la similitud

print("Similitudes con documentos:", similitud.flatten())  # Imprimimos las similitudes

# Ejemplo de aplicación real: En la recuperación de información, la vectorización TF-IDF y la similitud coseno pueden ser utilizadas para buscar documentos relevantes en una colección, considerando la frecuencia de términos y su importancia.
