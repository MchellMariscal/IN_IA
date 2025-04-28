# Equivalencia entre (p ∧ q) ↔ ¬(¬p ∨ ¬q) (Ley de De Morgan)
from itertools import product

def verificar_equivalencia():
    print("p\tq\t(p ∧ q)\t¬(¬p ∨ ¬q)\t¿Equivalentes?")
    for p, q in product([True, False], repeat=2):
        izquierda = p and q
        derecha = not (not p or not q)
        print(f"{p}\t{q}\t{izquierda}\t{derecha}\t{izquierda == derecha}")

verificar_equivalencia()
