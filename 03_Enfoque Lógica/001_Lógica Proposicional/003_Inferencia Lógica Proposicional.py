# Inferencia: Modus Ponens
def modus_ponens(p, p_implies_q):
    if p and p_implies_q:
        return True
    return False

p = True
p_implies_q = True
q = modus_ponens(p, p_implies_q)
print("¿Se puede inferir Q?", q)
