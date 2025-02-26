# 4.6. Sección 6 - Tuplas y Diccionarios

# 4.6.1 Tipos de secuencia y mutabilidad
# Ejemplo de secuencias mutables e inmutables
def mostrar_mutabilidad():
    lista = [1, 2, 3]
    tupla = (1, 2, 3)
    lista.append(4)  # Esto funciona
    try:
        tupla.append(4)  # Esto generará un error
    except AttributeError:
        print("No se puede modificar una tupla porque es inmutable.")
    print("Lista mutable:", lista)
    print("Tupla inmutable:", tupla)

# 4.6.2 Tuplas
# Ejemplo de uso de tuplas
def ejemplo_tuplas():
    coordenadas = (10.5, 20.3)
    print("Coordenadas:", coordenadas)
    print("Latitud:", coordenadas[0], "Longitud:", coordenadas[1])

# 4.6.3 Diccionarios
# Ejemplo de diccionario
def ejemplo_diccionario():
    persona = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}
    print("Información de la persona:", persona)
    print("Nombre:", persona["nombre"])  # Accediendo a un valor específico

# 4.6.4 Métodos y funciones de los diccionarios
def metodos_diccionario():
    dicc = {"a": 1, "b": 2, "c": 3}
    print("Claves:", dicc.keys())
    print("Valores:", dicc.values())
    print("Elementos:", dicc.items())
    dicc.pop("b")
    print("Diccionario después de eliminar 'b':", dicc)

# 4.6.5 Las tuplas y los diccionarios pueden trabajar juntos
def tuplas_y_diccionarios():
    lista_de_pares = [("nombre", "Ana"), ("edad", 25), ("ciudad", "Barcelona")]
    diccionario = dict(lista_de_pares)
    print("Diccionario creado desde una lista de tuplas:", diccionario)

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("\n--- Mutabilidad ---")
    mostrar_mutabilidad()
    
    print("\n--- Tuplas ---")
    ejemplo_tuplas()
    
    print("\n--- Diccionarios ---")
    ejemplo_diccionario()
    
    print("\n--- Métodos de diccionarios ---")
    metodos_diccionario()
    
    print("\n--- Tuplas y Diccionarios ---")
    tuplas_y_diccionarios()
