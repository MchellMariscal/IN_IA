class Taxonomia:
    def __init__(self):
        self.categorias = {
            "Frutas": ["Manzana", "Banana", "Mango"],
            "Verduras": ["Zanahoria", "Espinaca"],
            "Tecnología": ["Laptop", "Smartphone"]
        }

    def mostrar(self):
        for categoria, objetos in self.categorias.items():
            print(f"{categoria}: {', '.join(objetos)}")

tax = Taxonomia()
tax.mostrar()
