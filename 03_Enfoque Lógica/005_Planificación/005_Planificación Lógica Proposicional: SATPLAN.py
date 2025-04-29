# Simulación simplificada del uso de un SAT solver (no se usa un solver real)
variables = {"P": True, "Q": False}
clauses = [["P", "~Q"], ["Q"]]

def evaluate_clause(clause, assignment):
    return any((var.startswith("~") and not assignment[var[1:]]) or (not var.startswith("~") and assignment[var]) for var in clause)

satisfiable = all(evaluate_clause(c, variables) for c in clauses)
print("¿SATPLAN tiene solución?", satisfiable)
