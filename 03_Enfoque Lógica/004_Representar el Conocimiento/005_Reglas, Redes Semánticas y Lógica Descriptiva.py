class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

    def agregar_relacion(self, tipo, destino):
        self.atributos[tipo] = destino

canario = Nodo("Canario")
canario.agregar_relacion("es_un", "Ave")
canario.agregar_relacion("color", "amarillo")
print(f"{canario.nombre} es un {canario.atributos['es_un']} de color {canario.atributos['color']}.")
