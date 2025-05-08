# Diagnóstico simple: si coche_no_arranca → revisar_batería
def diagnostico(coche_no_arranca):
    if coche_no_arranca:  # Si el coche no arranca
        return "Revisar batería"  # Revisar la batería
    else:
        return "Todo funciona bien"  # Todo funciona bien

print(diagnostico(True))  # Imprimimos el diagnóstico

# Ejemplo de aplicación real: En los sistemas de diagnóstico, las reglas de diagnóstico pueden ser utilizadas para identificar problemas en sistemas, considerando las causas y efectos de los síntomas.
