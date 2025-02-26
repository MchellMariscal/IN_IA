# 4.4. Sección 4 - Alcances en Python

# 4.4.1 Funciones y alcances
def funcion_local():
    variable_local = "Soy una variable local"
    return variable_local

# 4.4.2 Funciones y alcances: la palabra clave global
variable_global = "Soy una variable global"

def modificar_global():
    global variable_global
    variable_global = "He sido modificada"

# 4.4.3 Cómo interactúa la función con sus argumentos
def modificar_lista(lista):
    lista.append("Nuevo elemento")
    return lista

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("\n--- Funciones y alcances ---")
    print("Valor retornado por la función local:", funcion_local())
    
    print("\n--- Funciones y palabra clave global ---")
    print("Antes de modificar:", variable_global)
    modificar_global()
    print("Después de modificar:", variable_global)
    
    print("\n--- Interacción con argumentos ---")
    mi_lista = ["Elemento 1", "Elemento 2"]
    print("Antes de modificar:", mi_lista)
    print("Después de modificar:", modificar_lista(mi_lista))