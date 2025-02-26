# 3.5. Sección 5 - Ordenamiento de listas: Algoritmo Burbuja

# 3.5.1 Ordenamiento Burbuja
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# 3.5.2 Ordenando una lista
def ordenar_lista():
    lista = [int(x) for x in input("Ingresa números separados por espacio: ").split()]
    print("Lista original:", lista)
    print("Lista ordenada:", ordenamiento_burbuja(lista))

# 3.5.3 El ordenamiento burbuja - versión interactiva
def ordenamiento_burbuja_interactivo():
    lista = [int(x) for x in input("Ingresa números separados por espacio: ").split()]
    print("Lista original:", lista)
    pasos = []
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                pasos.append(lista[:])
    for i, paso in enumerate(pasos, 1):
        print(f"Paso {i}: {paso}")
    print("Lista ordenada:", lista)

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("\n--- Ordenamiento Burbuja ---")
    ordenar_lista()
    
    print("\n--- Ordenamiento Burbuja Interactivo ---")
    ordenamiento_burbuja_interactivo()
