# 4.2. Sección 2 - Cómo se comunican las funciones con su entorno

# 4.2.1 Funciones parametrizadas
def funcion_parametrizada(nombre):
    print(f"Hola, {nombre}! Bienvenido a la programación con funciones.")

# 4.2.2 Paso de parámetros posicionales
def suma(a, b):
    return a + b

# 4.2.3 Paso de argumentos de palabra clave
def informacion_persona(nombre, edad):
    print(f"Nombre: {nombre}, Edad: {edad}")

# 4.2.4 Mezclando argumentos posicionales y de palabras clave
def datos_completos(nombre, edad, ciudad="Desconocida"):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# 4.2.5 Funciones parametrizadas - más detalles
def calcular_precio(base, impuesto=0.21, descuento=0):
    precio_final = base + (base * impuesto) - descuento
    return precio_final

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("\n--- Funciones parametrizadas ---")
    funcion_parametrizada("Carlos")
    
    print("\n--- Paso de parámetros posicionales ---")
    print("Suma de 10 + 5:", suma(10, 5))
    
    print("\n--- Paso de argumentos de palabra clave ---")
    informacion_persona(nombre="Ana", edad=25)
    
    print("\n--- Mezclando argumentos posicionales y de palabras clave ---")
    datos_completos("Luis", 30, ciudad="Madrid")
    
    print("\n--- Funciones parametrizadas - más detalles ---")
    print("Precio final con impuesto y descuento:", calcular_precio(100, descuento=10))

