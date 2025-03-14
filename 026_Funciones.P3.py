# 4.3. Sección 3 - Devolviendo el resultado de una función

# 4.3.1 Efectos y resultados: la instrucción return
def cuadrado(numero):
    return numero ** 2

# 4.3.2 Unas pocas palabras sobre None
def mensaje_condicional(valor):
    if valor > 0:
        return "Número positivo"
    elif valor < 0:
        return "Número negativo"
    else:
        return None

# 4.3.3 Efectos y resultados: listas y funciones
def duplicar_lista(lista):
    return [elemento * 2 for elemento in lista]

# 4.3.4 LAB Un año bisiesto: escribiendo tus propias funciones
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# 4.3.5 LAB Cuántos días: escribiendo y usando tus propias funciones
def dias_en_mes(mes, anio):
    dias_por_mes = {1: 31, 2: 29 if es_bisiesto(anio) else 28, 3: 31, 4: 30, 5: 31, 6: 30,
                    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return dias_por_mes.get(mes, "Mes inválido")

# 4.3.6 LAB Día del año: escribiendo y usando tus propias funciones
def dia_del_anio(dia, mes, anio):
    return sum(dias_en_mes(m, anio) for m in range(1, mes)) + dia

# 4.3.7 LAB Números primos - cómo encontrarlos
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# 4.3.8 LAB Conversión del consumo de combustible
def convertir_consumo(litros_100km):
    return 235.214583 / litros_100km

# Ejecutar los ejercicios
if __name__ == "__main__":
    print("\n--- Efectos y resultados: return ---")
    print("Cuadrado de 5:", cuadrado(5))
    
    print("\n--- Unas pocas palabras sobre None ---")
    print("Resultado para 0:", mensaje_condicional(0))
    
    print("\n--- Listas y funciones ---")
    print("Doble de [1, 2, 3]:", duplicar_lista([1, 2, 3]))
    
    print("\n--- Año bisiesto ---")
    print("2024 es bisiesto?", es_bisiesto(2024))
    
    print("\n--- Cuántos días tiene febrero de 2023? ---")
    print("Días en febrero 2023:", dias_en_mes(2, 2023))
    
    print("\n--- Día del año ---")
    print("El 15 de marzo es el día:", dia_del_anio(15, 3, 2023))
    
    print("\n--- Números primos ---")
    print("¿Es 17 un número primo?", es_primo(17))
    
    print("\n--- Conversión de consumo de combustible ---")
    print("Litros/100km a MPG (8L/100km):", convertir_consumo(8))

