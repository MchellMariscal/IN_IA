# 4.7. Sección 7 - Excepciones

# 4.7.1 Errores - el pan diario del desarrollador
# Ejemplo de manejo de errores con try-except
def manejo_errores():
    try:
        x = 1 / 0  # Error intencional
    except ZeroDivisionError as e:
        print("Error atrapado:", e)

# 4.7.2 Cuando los datos no son lo que deberían ser
def validar_entrada(valor):
    if not isinstance(valor, int):
        raise ValueError("Se esperaba un número entero.")
    print("Valor válido:", valor)

# 4.7.3 La rama try-except
def ejemplo_try_except():
    try:
        archivo = open("archivo.txt", "r")
        contenido = archivo.read()
    except FileNotFoundError:
        print("El archivo no existe.")
    finally:
        print("Fin del manejo de archivos.")

# 4.7.4 La excepción confirma la regla
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero."

# 4.7.5 Cómo lidiar con más de una excepción
def multiples_excepciones():
    try:
        x = int("hola")
    except (ValueError, TypeError) as e:
        print("Error detectado:", e)

# 4.7.6 La excepción predeterminada y cómo usarla
def excepcion_general():
    try:
        resultado = 10 / "a"
    except Exception as e:
        print("Error inesperado:", e)

# 4.7.7 Algunas excepciones útiles
def excepciones_utiles():
    try:
        lista = [1, 2, 3]
        print(lista[5])
    except IndexError:
        print("Índice fuera de rango.")

# 4.7.8 ¿Por qué no puedes evitar probar tu código?
def prueba_codigo():
    try:
        assert 2 + 2 == 5, "Matemáticas incorrectas"
    except AssertionError as e:
        print("Error de aserción:", e)

# 4.7.9 Cuando Python cierra los ojos
def error_oculto():
    try:
        import modulo_inexistente
    except ModuleNotFoundError:
        print("El módulo no existe.")

# 4.7.10 Pruebas, pruebas y más pruebas
def prueba_manual():
    try:
        x = int(input("Introduce un número: "))
        print("Número ingresado:", x)
    except ValueError:
        print("Entrada no válida.")

# 4.7.11 Print debugging (depuración)
def debug_con_print():
    try:
        x = int("10a")
    except ValueError as e:
        print("Error detectado:", e)
        print("Depurando variable x")

# 4.7.12 Algunos consejos útiles
def consejos_excepciones():
    try:
        with open("archivo.txt", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no está disponible.")

# 4.7.13 Pruebas unitarias - un mayor nivel de codificación
import unittest

def suma(a, b):
    return a + b

class TestFunciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)

if __name__ == "__main__":
    print("\n--- Manejo de Errores ---")
    manejo_errores()
    
    print("\n--- Validar Entrada ---")
    try:
        validar_entrada("texto")
    except ValueError as e:
        print(e)
    
    print("\n--- Try-Except ---")
    ejemplo_try_except()
    
    print("\n--- División Segura ---")
    print(dividir(10, 0))
    
    print("\n--- Múltiples Excepciones ---")
    multiples_excepciones()
    
    print("\n--- Excepción General ---")
    excepcion_general()
    
    print("\n--- Excepciones Útiles ---")
    excepciones_utiles()
    
    print("\n--- Prueba de Código ---")
    prueba_codigo()
    
    print("\n--- Error Oculto ---")
    error_oculto()
    
    print("\n--- Pruebas Manuales ---")
    prueba_manual()
    
    print("\n--- Debug con Print ---")
    debug_con_print()
    
    print("\n--- Consejos de Excepciones ---")
    consejos_excepciones()
    
    print("\n--- Pruebas Unitarias ---")
    unittest.main()

