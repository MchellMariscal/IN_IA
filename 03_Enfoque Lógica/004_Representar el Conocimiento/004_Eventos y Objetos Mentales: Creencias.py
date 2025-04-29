class Creencias:
    def __init__(self):
        self.creencias = {"llueve": True, "tráfico": False}

    def actualizar(self, creencia, valor):
        self.creencias[creencia] = valor

    def consultar(self, creencia):
        return self.creencias.get(creencia, "Desconocido")

mente = Creencias()
print("¿Cree que llueve?", mente.consultar("llueve"))
mente.actualizar("tráfico", True)
