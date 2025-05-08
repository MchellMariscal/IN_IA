# Inferencia: Modus Ponens
def modus_ponens(p, p_implies_q):
    if p and p_implies_q:
        return True
    return False

p = True
p_implies_q = True
q = modus_ponens(p, p_implies_q)
print("¿Se puede inferir Q?", q)
# Inferencia: Modus Ponens
def modus_ponens(p, p_implies_q):
    if p and p_implies_q:  # Si p es verdadero y p implica q es verdadero
        return True  # Entonces q es verdadero
    return False  # En caso contrario, q es falso

p = True  # Valor de verdad de p
p_implies_q = True  # Valor de verdad de p → q
q = modus_ponens(p, p_implies_q)  # Aplicamos el modus ponens
print("¿Se puede inferir Q?", q)  # Imprimimos el resultado de la inferencia

# Ejemplo de aplicación real: En la lógica proposicional, el modus ponens puede ser utilizado para inferir nuevas proposiciones a partir de reglas y hechos conocidos, considerando la validez de las premisas.
