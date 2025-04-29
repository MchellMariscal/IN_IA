def logica_modal(posible, necesario):
    if necesario:
        return "Es necesario que sea verdadero."
    elif posible:
        return "Es posible que sea verdadero."
    return "No es ni necesario ni posible."
