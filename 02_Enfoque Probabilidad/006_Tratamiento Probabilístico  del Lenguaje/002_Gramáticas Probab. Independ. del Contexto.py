import nltk
from nltk import Nonterminal, induce_pcfg
from nltk.grammar import Production

# Producciones
producciones = [
    Production(Nonterminal('S'), [Nonterminal('NP'), Nonterminal('VP')]),
    Production(Nonterminal('NP'), ['el', 'gato']),
    Production(Nonterminal('VP'), ['duerme']),
]

# Inducir una gramática PCFG
S = Nonterminal('S')
gramatica = induce_pcfg(S, producciones)

print("Gramática PCFG:")
print(gramatica)
