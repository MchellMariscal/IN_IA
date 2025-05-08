import nltk
from nltk import Nonterminal, induce_pcfg
from nltk.grammar import Production

# Producciones de la gramática
producciones = [
    Production(Nonterminal('S'), [Nonterminal('NP'), Nonterminal('VP')]),  # S → NP VP
    Production(Nonterminal('NP'), ['el', 'gato']),  # NP → el gato
    Production(Nonterminal('VP'), ['duerme']),  # VP → duerme
]

# Inducir una gramática PCFG (Gramática Probabilística de Estructura de Frase)
S = Nonterminal('S')  # Símbolo inicial
gramatica = induce_pcfg(S, producciones)  # Inducimos la gramática

print("Gramática PCFG:")  # Imprimimos la gramática
print(gramatica)  # Imprimimos la gramática

# Ejemplo de aplicación real: En la generación de lenguaje, las gramáticas probabilísticas independientes del contexto pueden ser utilizadas para modelar la estructura de las oraciones, considerando las reglas de producción y sus probabilidades.
