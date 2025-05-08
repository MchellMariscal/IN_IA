from sympy import symbols, diff, sin, cos, exp

# Definir la variable simbólica
x = symbols('x')

# Ejemplo 1: f(x) = sin(x^2)
f = sin(x**2)  # Definimos la función
derivada_f = diff(f, x)  # Calculamos la derivada usando la regla de la cadena
print("Derivada de sin(x^2):", derivada_f)  # Imprimimos la derivada

# Ejemplo 2: f(x) = e^(3x + 1)
f2 = exp(3*x + 1)  # Definimos la función
derivada_f2 = diff(f2, x)  # Calculamos la derivada usando la regla de la cadena
print("Derivada de e^(3x + 1):", derivada_f2)  # Imprimimos la derivada

# Ejemplo 3: f(x) = cos(x^3 + x)
f3 = cos(x**3 + x)  # Definimos la función
derivada_f3 = diff(f3, x)  # Calculamos la derivada usando la regla de la cadena
print("Derivada de cos(x^3 + x):", derivada_f3)  # Imprimimos la derivada

# Ejemplo de aplicación real: En la física, la regla de la cadena puede ser utilizada para calcular derivadas de funciones compuestas, como en el análisis de movimiento y fuerzas.
