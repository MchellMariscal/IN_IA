def orden_superior_ejemplo():
    def aplicar_funcion(f, valores):
        return [f(v) for v in valores]

    print(aplicar_funcion(lambda x: x**2, [1, 2, 3, 4]))
