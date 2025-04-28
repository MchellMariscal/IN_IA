# Unificación simple de predicados
def unificar(pred1, pred2):
    if pred1.split("(")[0] == pred2.split("(")[0]:
        return "Unificación exitosa"
    else:
        return "No se puede unificar"

print(unificar("padre(juan, maria)", "padre(X, maria)"))
