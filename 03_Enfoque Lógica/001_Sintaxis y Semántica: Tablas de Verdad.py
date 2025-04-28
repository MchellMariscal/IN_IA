from itertools import product

# Definir una función para tabla de verdad de p → q
def tabla_verdad():
    print("p\tq\tp → q")
    for p, q in product([True, False], repeat=2):
        implicacion = (not p) or q
        print(f"{p}\t{q}\t{implicacion}")

tabla_verdad()
