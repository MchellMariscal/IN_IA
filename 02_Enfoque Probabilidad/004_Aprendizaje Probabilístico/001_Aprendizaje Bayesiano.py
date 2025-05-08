# Probabilidad a priori de que un mensaje sea SPAM
P_spam = 0.2
P_no_spam = 0.8  # Probabilidad a priori de que un mensaje no sea SPAM

# Probabilidad de que una palabra aparezca en un mensaje SPAM o no SPAM
P_palabra_spam = 0.9  # Probabilidad de la palabra dado SPAM
P_palabra_no_spam = 0.1  # Probabilidad de la palabra dado no SPAM

# Probabilidad total de la palabra (evidencia)
P_palabra = P_spam * P_palabra_spam + P_no_spam * P_palabra_no_spam

# Probabilidad a posteriori de que un mensaje sea SPAM dado que contiene la palabra
P_spam_palabra = (P_spam * P_palabra_spam) / P_palabra

print(f"Probabilidad de SPAM dado la palabra: {P_spam_palabra:.4f}")  # Imprimimos la probabilidad

# Ejemplo de aplicación real: En el filtrado de correo electrónico, el aprendizaje bayesiano puede ser utilizado para clasificar mensajes como SPAM o no SPAM, considerando la probabilidad de ciertas palabras en cada tipo de mensaje.
