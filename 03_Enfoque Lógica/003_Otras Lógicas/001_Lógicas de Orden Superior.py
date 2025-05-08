def orden_superior_ejemplo():
    # Función de orden superior que aplica una función a una lista de valores
    def aplicar_funcion(f, valores):
        return [f(v) for v in valores]  # Aplicamos la función f a cada valor en la lista

    # Ejemplo: aplicamos una función lambda que eleva al cuadrado
    print(aplicar_funcion(lambda x: x**2, [1, 2, 3, 4]))  # Imprimimos el resultado de aplicar la función

# Ejemplo de aplicación real: En la programación funcional, las lógicas de orden superior pueden ser utilizadas para manipular funciones como argumentos, permitiendo la abstracción y reutilización de código.
