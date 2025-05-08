# Simulación de ejecución con vigilancia y replanificación
estado = "inicial"  # Estado inicial
plan = ["ir_a_tienda", "comprar_pan"]  # Plan inicial

for paso in plan:  # Para cada paso en el plan
    if paso == "comprar_pan" and estado != "en_tienda":  # Si no estamos en la tienda
        print("¡Error! No estás en la tienda. Replanificando...")  # Imprimimos un mensaje de error
        plan.insert(1, "ir_a_tienda")  # Replanificamos añadiendo "ir_a_tienda"
        break  # Terminamos el plan
    print("Ejecutando:", paso)  # Imprimimos el paso actual
    estado = "en_tienda" if paso == "ir_a_tienda" else estado  # Actualizamos el estado

# Ejemplo de aplicación real: En la ejecución de planes, la vigilancia y replanificación pueden ser utilizadas para manejar errores y cambios en el entorno, considerando la ejecución y replanificación de acciones.
