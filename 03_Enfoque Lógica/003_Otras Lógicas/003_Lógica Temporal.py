def logica_temporal():
    estados = ['inicio', 'procesando', 'final']
    for tiempo, estado in enumerate(estados):
        print(f"En t={tiempo}, el sistema está en estado: {estado}")
