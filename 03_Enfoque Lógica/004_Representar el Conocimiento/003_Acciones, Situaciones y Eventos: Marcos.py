class Marco:
    def __init__(self, tipo, agente, objeto, lugar):
        self.tipo = tipo
        self.agente = agente
        self.objeto = objeto
        self.lugar = lugar

    def describir(self):
        return f"El {self.agente} realiza una acción de {self.tipo} con {self.objeto} en {self.lugar}."

compra = Marco("compra", "cliente", "producto", "supermercado")
print(compra.describir())
