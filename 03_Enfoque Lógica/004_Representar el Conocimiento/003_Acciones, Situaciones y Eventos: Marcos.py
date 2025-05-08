class Marco:
    def __init__(self, tipo, agente, objeto, lugar):
        # Definimos un marco con tipo, agente, objeto y lugar
        self.tipo = tipo  # Tipo de acción
        self.agente = agente  # Agente que realiza la acción
        self.objeto = objeto  # Objeto de la acción
        self.lugar = lugar  # Lugar de la acción

    def describir(self):
        return f"El {self.agente} realiza una acción de {self.tipo} con {self.objeto} en {self.lugar}."  # Descripción del marco

compra = Marco("compra", "cliente", "producto", "supermercado")  # Creamos una instancia de un marco
print(compra.describir())  # Imprimimos la descripción del marco

# Ejemplo de aplicación real: En la representación del conocimiento, los marcos pueden ser utilizados para describir acciones, situaciones y eventos, considerando los componentes y relaciones involucradas.
