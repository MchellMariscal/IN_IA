class Ontologia:
    def __init__(self):
        self.ontologia = {
            "SerVivo": ["Animal", "Planta"],
            "Animal": ["Mamífero", "Ave"],
            "Mamífero": ["Perro", "Gato"],
            "Ave": ["Canario", "Pingüino"]
        }

    def obtener_descendencia(self, concepto):
        descendencia = self.ontologia.get(concepto, [])
        for hijo in descendencia:
            descendencia += self.ontologia.get(hijo, [])
        return list(set(descendencia))

ont = Ontologia()
print("Descendientes de Animal:", ont.obtener_descendencia("Animal"))
