from sklearn.cluster import KMeans
import numpy as np

# Datos de ejemplo
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

# Aplicar K-Means para agrupar los datos
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)  # Inicializamos y ajustamos el modelo
print("Etiquetas de los grupos:", kmeans.labels_)  # Imprimimos las etiquetas de los grupos

# Ejemplo de aplicación real: En el análisis de mercado, el agrupamiento no supervisado puede ser utilizado para segmentar clientes en grupos basados en su comportamiento de compra, considerando las características de los datos sin etiquetar.
