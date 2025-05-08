class Taxonomia:
    def __init__(self):
        # Definimos una taxonomía simple con categorías y objetos
        self.categorias = {
            "Frutas": ["Manzana", "Banana", "Mango"],  # Frutas tiene como objetos a Manzana, Banana y Mango
            "Verduras": ["Zanahoria", "Espinaca"],  # Verduras tiene como objetos a Zanahoria y Espinaca
            "Tecnología": ["Laptop", "Smartphone"]  # Tecnología tiene como objetos a Laptop y Smartphone
        }

    def mostrar(self):
        for categoria, objetos in self.categorias.items():  # Para cada categoría
            print(f"{categoria}: {', '.join(objetos)}")  # Imprimimos la categoría y sus objetos

tax = Taxonomia()  # Creamos una instancia de la taxonomía
tax.mostrar()  # Mostramos la taxonomía

# Ejemplo de aplicación real: En la organización del conocimiento, las taxonomías pueden ser utilizadas para clasificar y organizar objetos en categorías, considerando las relaciones de pertenencia.
