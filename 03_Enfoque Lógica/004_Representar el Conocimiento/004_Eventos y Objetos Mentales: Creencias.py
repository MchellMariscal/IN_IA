class Creencias:
    def __init__(self):
        # Definimos un conjunto de creencias iniciales
        self.creencias = {"llueve": True, "tráfico": False}  # Creencias iniciales

    def actualizar(self, creencia, valor):
        self.creencias[creencia] = valor  # Actualizamos una creencia

    def consultar(self, creencia):
        return self.creencias.get(creencia, "Desconocido")  # Consultamos una creencia

mente = Creencias()  # Creamos una instancia de creencias
print("¿Cree que llueve?", mente.consultar("llueve"))  # Consultamos una creencia
mente.actualizar("tráfico", True)  # Actualizamos una creencia

# Ejemplo de aplicación real: En los sistemas de creencias, las creencias pueden ser utilizadas para representar y actualizar el conocimiento sobre el mundo, considerando las percepciones y experiencias.
