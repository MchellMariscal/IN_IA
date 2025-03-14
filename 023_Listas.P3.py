# 3.7. Sección 7 - Aplicaciones avanzadas de listas

# 3.7.1 Listas dentro de listas
def listas_dentro_de_listas():
    lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Lista anidada:", lista_anidada)
    print("Primer sublista:", lista_anidada[0])
    print("Elemento en la posición [1][2]:", lista_anidada[1][2])

# 3.7.2 Arreglos de dos dimensiones
def arreglos_dos_dimensiones():
    matriz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print("Matriz 3x3 generada:")
    for fila in matriz:
        print(fila)

# 3.7.3 Naturaleza multidimensional de las listas: aplicaciones avanzadas
def aplicaciones_multidimensionales():
    matriz = [[i + j for j in range(3)] for i in range(3)]
    print("Matriz original:")
    for fila in matriz:
        print(fila)
    
    transpuesta = [[fila[i] for fila in matriz] for i in range(3)]
    print("Matriz transpuesta:")
    for fila in transpuesta:
        print(fila)

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("\n--- Listas dentro de listas ---")
    listas_dentro_de_listas()
    
    print("\n--- Arreglos de dos dimensiones ---")
    arreglos_dos_dimensiones()
    
    print("\n--- Naturaleza multidimensional de las listas: aplicaciones avanzadas ---")
    aplicaciones_multidimensionales()
