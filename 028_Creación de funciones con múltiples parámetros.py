# 4.5. Sección 5 - Creación de funciones con múltiples parámetros

# 4.5.1 Ejemplo de función: Cálculo del IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 4.5.2 Ejemplo de función: Área de un triángulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# 4.5.3 Ejemplo de función: Factorial
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# 4.5.4 Números Fibonacci
def fibonacci(n):
    secuencia = [0, 1]
    for _ in range(n - 2):
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]

# 4.5.5 Recursividad: Factorial recursivo
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("\n--- Cálculo del IMC ---")
    print("IMC de una persona de 70kg y 1.75m:", calcular_imc(70, 1.75))
    
    print("\n--- Área de un triángulo ---")
    print("Área de un triángulo con base 10 y altura 5:", area_triangulo(10, 5))
    
    print("\n--- Factorial ---")
    print("Factorial de 5:", factorial(5))
    
    print("\n--- Fibonacci ---")
    print("Primeros 10 números de Fibonacci:", fibonacci(10))
    
    print("\n--- Factorial recursivo ---")
    print("Factorial de 5 (recursivo):", factorial_recursivo(5))

