# Simulación de ejecución con vigilancia y replanificación
estado = "inicial"
plan = ["ir_a_tienda", "comprar_pan"]

for paso in plan:
    if paso == "comprar_pan" and estado != "en_tienda":
        print("¡Error! No estás en la tienda. Replanificando...")
        plan.insert(1, "ir_a_tienda")
        break
    print("Ejecutando:", paso)
    estado = "en_tienda" if paso == "ir_a_tienda" else estado
