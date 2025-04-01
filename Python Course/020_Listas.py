# Ejercicio 1: ¿Por qué necesitamos listas?
def uso_listas():
    lista = ["manzana", "banana", "cereza", "durazno", "uva"]
    print("Lista de frutas:", lista)
    print("Tercer elemento:", lista[2])

# Ejercicio 2: Indexación de listas
def indexacion_listas():
    numeros = [10, 20, 30, 40, 50]
    print("Primer elemento:", numeros[0])
    print("Último elemento:", numeros[-1])
    print("Penúltimo elemento:", numeros[-2])

# Ejercicio 3: Acceso y modificación de listas
def modificar_listas():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dias[2] = "Día especial"
    dias.remove("Sábado")
    print("Lista de días modificada:", dias)

# Ejercicio 4: Agregando elementos a una lista
def agregar_elementos():
    colores = []
    colores.append("Rojo")
    colores.append("Azul")
    colores.append("Verde")
    colores.insert(0, "Negro")
    print("Lista de colores:", colores)

# Ejercicio 5: Funciones vs métodos
def funciones_vs_metodos():
    numeros = [4, 8, 1, 6, 9]
    print("Longitud de la lista:", len(numeros))
    print("Suma de elementos:", sum(numeros))
    print("Valor máximo:", max(numeros))
    print("Valor mínimo:", min(numeros))
    numeros.sort()
    print("Lista ordenada:", numeros)
    numeros.reverse()
    print("Lista invertida:", numeros)

# Ejercicio 6: Aplicación práctica
def lista_usuarios():
    nombres = [input("Ingresa un nombre: ") for _ in range(5)]
    print("Lista original:", nombres)
    nombres.sort()
    print("Lista ordenada:", nombres)
    nuevo_nombre = input("Ingresa un nuevo nombre: ")
    nombres.append(nuevo_nombre)
    print("Lista con nuevo nombre:", nombres)
    del nombres[1]
    print("Lista después de eliminar el segundo nombre:", nombres)

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("--- Uso de Listas ---")
    uso_listas()
    
    print("\n--- Indexación de Listas ---")
    indexacion_listas()
    
    print("\n--- Modificación de Listas ---")
    modificar_listas()
    
    print("\n--- Agregar Elementos ---")
    agregar_elementos()
    
    print("\n--- Funciones vs Métodos ---")
    funciones_vs_metodos()
    
    print("\n--- Lista de Usuarios ---")
    lista_usuarios()
