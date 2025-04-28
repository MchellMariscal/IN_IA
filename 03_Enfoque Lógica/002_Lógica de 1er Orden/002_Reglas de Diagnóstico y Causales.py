# Diagnóstico simple: si coche_no_arranca → revisar_batería
def diagnostico(coche_no_arranca):
    if coche_no_arranca:
        return "Revisar batería"
    else:
        return "Todo funciona bien"

print(diagnostico(True))
