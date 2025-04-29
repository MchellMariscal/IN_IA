def puede_volar(animal):
    excepciones = ["pingüino", "avestruz"]
    if animal in excepciones:
        return f"{animal} NO puede volar."
    return f"{animal} probablemente puede volar."

print(puede_volar("águila"))
print(puede_volar("pingüino"))
