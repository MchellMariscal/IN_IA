from sklearn.feature_extraction.text import TfidfVectorizer

# Documentos
docs = [
    "el gato duerme en la cama",
    "el perro corre en el parque",
    "los gatos y perros son animales"
]

# Vectorización TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

# Consulta
query = "gato cama"

query_vec = vectorizer.transform([query])

# Similaridad coseno
from sklearn.metrics.pairwise import cosine_similarity
similaridad = cosine_similarity(query_vec, X)

print("Similitudes con documentos:", similaridad.flatten())
