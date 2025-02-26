# 3.6. Sección 6 - Operaciones con listas

# 3.6.1 La vida al interior de las listas
def vida_en_listas():
    lista = [1, 2, 3, "Python", True, 3.14]
    print("Lista original:", lista)
    print("Primer elemento:", lista[0])
    print("Último elemento:", lista[-1])
    print("Sublista de los primeros tres elementos:", lista[:3])

# 3.6.2 Rebanadas Poderosas
def rebanadas_poderosas():
    lista = list(range(10))
    print("Lista original:", lista)
    print("Elementos del índice 2 al 6:", lista[2:7])
    print("Cada segundo elemento:", lista[::2])
    print("Lista invertida:", lista[::-1])

# 3.6.3 Rebanadas - índices negativos
def rebanadas_indices_negativos():
    lista = list("abcdefg")
    print("Lista original:", lista)
    print("Últimos tres elementos:", lista[-3:])
    print("Elementos excepto los dos últimos:", lista[:-2])

# 3.6.4 Los operadores in y not in
def operadores_in_not_in():
    lista = [10, 20, 30, 40]
    print("Lista:", lista)
    print("¿30 está en la lista?", 30 in lista)
    print("¿50 no está en la lista?", 50 not in lista)

# 3.6.5 Listas - algunos programas simples
def programas_simples():
    lista = [int(x) for x in input("Ingresa números separados por espacio: ").split()]
    print("Lista original:", lista)
    print("Suma de los elementos:", sum(lista))
    print("Máximo de la lista:", max(lista))
    print("Mínimo de la lista:", min(lista))

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("\n--- La vida al interior de las listas ---")
    vida_en_listas()
    
    print("\n--- Rebanadas Poderosas ---")
    rebanadas_poderosas()
    
    print("\n--- Rebanadas - índices negativos ---")
    rebanadas_indices_negativos()
    
    print("\n--- Los operadores in y not in ---")
    operadores_in_not_in()
    
    print("\n--- Listas - algunos programas simples ---")
    programas_simples()
