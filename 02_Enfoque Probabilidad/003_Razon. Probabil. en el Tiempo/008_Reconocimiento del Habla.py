# Supongamos dos palabras: "hola" y "ola"
palabras = ["hola", "ola"]
modelos = {
    "hola": ["h", "o", "l", "a"],  # Modelo para "hola"
    "ola": ["o", "l", "a"]  # Modelo para "ola"
}

# Función para reconocer el habla
def reconocer_habla(sonidos):
    mejores = []  # Lista para guardar los mejores resultados
    for palabra, modelo in modelos.items():  # Para cada palabra
        score = sum(1 for s, m in zip(sonidos, modelo) if s == m)  # Calculamos el score
        mejores.append((score, palabra))  # Guardamos el score y la palabra
    mejores.sort(reverse=True)  # Ordenamos los resultados
    return mejores[0][1]  # Devolvemos la palabra con el mejor score

# Ejemplo
entrada_usuario = ["o", "l", "a"]  # Entrada del usuario
resultado = reconocer_habla(entrada_usuario)  # Reconocemos el habla
print("Palabra reconocida:", resultado)  # Imprimimos la palabra reconocida

# Ejemplo de aplicación real: En el procesamiento de lenguaje natural, el reconocimiento del habla puede ser utilizado para transcribir y entender el habla humana, considerando los modelos de palabras y los sonidos recibidos.
