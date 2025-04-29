def decision_lluvia(prob_lluvia, valor_paraguas=1, costo_mojarse=5):
    utilidad_llevar = -valor_paraguas
    utilidad_no_llevar = -prob_lluvia * costo_mojarse
    if utilidad_llevar > utilidad_no_llevar:
        return "No llevar paraguas"
    return "Llevar paraguas"

print(decision_lluvia(0.6))
print(decision_lluvia(0.9))
