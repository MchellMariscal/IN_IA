# Ejercicio 1: Expresiones Lógicas

def expresiones_logicas():
    a = bool(int(input("Ingresa 1 para True o 0 para False (A): ")))
    b = bool(int(input("Ingresa 1 para True o 0 para False (B): ")))
    
    print(f"A AND B: {a and b}")
    print(f"A OR B: {a or b}")
    print(f"NOT A: {not a}")
    print(f"NOT B: {not b}")

# Ejercicio 2: Valores lógicos vs bits individuales
def valores_logicos_vs_bits():
    a = True
    b = False
    x = 0b1010  # 10 en binario
    y = 0b1100  # 12 en binario
    
    print(f"a AND b: {a and b}")
    print(f"a OR b: {a or b}")
    print(f"x & y (AND bit a bit): {bin(x & y)}")
    print(f"x | y (OR bit a bit): {bin(x | y)}")
    print(f"x ^ y (XOR bit a bit): {bin(x ^ y)}")

# Ejercicio 3: Operaciones bit a bit
def operaciones_bit_a_bit():
    num = int(input("Ingresa un número entero: "))
    print(f"Número en binario: {bin(num)}")
    print(f"num & 0b1010: {bin(num & 0b1010)}")
    print(f"num | 0b1010: {bin(num | 0b1010)}")
    print(f"num ^ 0b1010: {bin(num ^ 0b1010)}")
    print(f"~num (Negación): {bin(~num)}")

# Ejercicio 4: Desplazamiento de bits
def desplazamiento_bits():
    num = int(input("Ingresa un número entero: "))
    print(f"Número en binario: {bin(num)}")
    print(f"Desplazamiento a la izquierda (num << 2): {bin(num << 2)}")
    print(f"Desplazamiento a la derecha (num >> 2): {bin(num >> 2)}")

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("--- Expresiones Lógicas ---")
    expresiones_logicas()
    
    print("\n--- Valores lógicos vs Bits Individuales ---")
    valores_logicos_vs_bits()
    
    print("\n--- Operaciones Bit a Bit ---")
    operaciones_bit_a_bit()
    
    print("\n--- Desplazamiento de Bits ---")
    desplazamiento_bits()
