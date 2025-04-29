def no_monotonica():
    conocimiento = {"llueve": True}
    print("Inicial:", conocimiento)
    conocimiento["llueve"] = False  # nuevo conocimiento cambia el anterior
    print("Actualizado:", conocimiento)
