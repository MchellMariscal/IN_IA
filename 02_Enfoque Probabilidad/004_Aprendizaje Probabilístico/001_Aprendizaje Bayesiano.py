# Prior
P_spam = 0.2
P_no_spam = 0.8

# Likelihoods
P_palabra_spam = 0.9
P_palabra_no_spam = 0.1

# Evidencia
P_palabra = P_spam * P_palabra_spam + P_no_spam * P_palabra_no_spam

# Posterior
P_spam_palabra = (P_spam * P_palabra_spam) / P_palabra

print(f"Probabilidad de SPAM dado la palabra: {P_spam_palabra:.4f}")
