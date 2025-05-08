class Nodo:
    def __init__(self, nombre):
        # Definimos un nodo con nombre y atributos
        self.nombre = nombre  # Nombre del nodo
        self.atributos = {}  # Atributos del nodo

    def agregar_relacion(self, tipo, destino):
        self.atributos[tipo] = destino  # Agregamos una relación al nodo

canario = Nodo("Canario")  # Creamos una instancia de un nodo
canario.agregar_relacion("es_un", "Ave")  # Agregamos una relación
canario.agregar_relacion("color", "amarillo")  # Agregamos otra relación
print(f"{canario.nombre} es un {canario.atributos['es_un']} de color {canario.atributos['color']}.")  # Imprimimos la descripción del nodo

# Ejemplo de aplicación real: En la representación del conocimiento, las redes semánticas pueden ser utilizadas para representar relaciones entre conceptos, considerando los nodos y sus atributos.
