# 4.1. Sección 1 - Funciones

# 4.1.1 ¿Por qué necesitamos funciones?
def por_que_funciones():
    print("Las funciones permiten reutilizar código y hacerlo más modular y organizado.")

# 4.1.2 Descomposición
def descomposicion():
    def suma(a, b):
        return a + b
    
    def resta(a, b):
        return a - b
    
    print("Suma de 5 + 3:", suma(5, 3))
    print("Resta de 5 - 3:", resta(5, 3))

# 4.1.3 ¿De dónde provienen las funciones?
def de_donde_provienen_las_funciones():
    print("Las funciones pueden ser integradas en Python (como print()), definidas por el usuario o importadas de módulos.")

# 4.1.4 Tu primera función
def mi_primera_funcion():
    print("¡Hola, esta es mi primera función en Python!")

# 4.1.5 Cómo funcionan las funciones
def como_funcionan_las_funciones():
    def cuadrado(numero):
        return numero ** 2
    
    print("El cuadrado de 4 es:", cuadrado(4))
    print("El cuadrado de 7 es:", cuadrado(7))

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("\n--- ¿Por qué necesitamos funciones? ---")
    por_que_funciones()
    
    print("\n--- Descomposición ---")
    descomposicion()
    
    print("\n--- ¿De dónde provienen las funciones? ---")
    de_donde_provienen_las_funciones()
    
    print("\n--- Tu primera función ---")
    mi_primera_funcion()
    
    print("\n--- Cómo funcionan las funciones ---")
    como_funcionan_las_funciones()
