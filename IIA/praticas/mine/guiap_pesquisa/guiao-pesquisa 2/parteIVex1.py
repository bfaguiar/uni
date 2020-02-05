from constraintsearch import *

from pprint import pprint

# Guiaop TP IV.4b) 
valores = ['azul', 'vermelho', 'verde', 'amarelo']
variaveis = ['A', 'B', 'C', 'D', 'E', 'F']

# grafo: ver no caderno.

dominios = {var:valores for var in variaveis}
arcos = [('A','B'),('B','C'),('C','F'),('D','F'),('D','A')] + [(v, 'E') for v in variaveis if v != 'E']

arcos += [(v2, v1) for (v2, v1) in arcos] ## acrescenta os arcos inversos (bidirecionais).
grafo = {a:(lambda v1, x1, v2, x2: x1 != x2) for a in arcos} ## o lambda é uma funcao, passa a funcao.   

##
pprint(dominios)
cores = ConstraintSearch(dominios, grafo)
#dominios[] 

print(cores.search())

