class Ontologia:
    def __init__(self):
        # Definimos una ontología simple con relaciones jerárquicas
        self.ontologia = {
            "SerVivo": ["Animal", "Planta"],  # SerVivo tiene como descendientes a Animal y Planta
            "Animal": ["Mamífero", "Ave"],  # Animal tiene como descendientes a Mamífero y Ave
            "Mamífero": ["Perro", "Gato"],  # Mamífero tiene como descendientes a Perro y Gato
            "Ave": ["Canario", "Pingüino"]  # Ave tiene como descendientes a Canario y Pingüino
        }

    def obtener_descendencia(self, concepto):
        descendencia = self.ontologia.get(concepto, [])  # Obtenemos los descendientes directos del concepto
        for hijo in descendencia:  # Para cada descendiente directo
            descendencia += self.ontologia.get(hijo, [])  # Obtenemos los descendientes de los descendientes
        return list(set(descendencia))  # Devolvemos la lista de descendientes sin duplicados

ont = Ontologia()  # Creamos una instancia de la ontología
print("Descendientes de Animal:", ont.obtener_descendencia("Animal"))  # Imprimimos los descendientes de Animal

# Ejemplo de aplicación real: En la ingeniería del conocimiento, las ontologías pueden ser utilizadas para representar y organizar el conocimiento en un dominio específico, considerando las relaciones jerárquicas entre conceptos.
