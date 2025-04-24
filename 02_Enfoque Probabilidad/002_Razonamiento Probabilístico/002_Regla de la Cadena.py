from sympy import symbols, diff, sin, cos, exp

# Definir la variable
x = symbols('x')

# Ejemplo 1: f(x) = sin(x^2)
f = sin(x**2)
derivada_f = diff(f, x)
print("Derivada de sin(x^2):", derivada_f)

# Ejemplo 2: f(x) = e^(3x + 1)
f2 = exp(3*x + 1)
derivada_f2 = diff(f2, x)
print("Derivada de e^(3x + 1):", derivada_f2)

# Ejemplo 3: f(x) = cos(x^3 + x)
f3 = cos(x**3 + x)
derivada_f3 = diff(f3, x)
print("Derivada de cos(x^3 + x):", derivada_f3)
