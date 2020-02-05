from constraintsearch import *

# 4 a)
def maps_constraint(var1, col1, var2, col2):
	
	if col1==col2:
		return False
	return True

cg = {('A','B'):maps_constraint, ('A','D'):maps_constraint,('A','E'):maps_constraint, \
('B','E'):maps_constraint,('B','C'):maps_constraint,('C','E'):maps_constraint,('D','E'):maps_constraint }

colors = [1,2,3]
domains = { l:colors for l in ['A','B','C','D','E'] }

cs = ConstraintSearch(domains,cg)

print(cs.search())

# 4 b)

cg = {('A','B'):maps_constraint,('A','E'):maps_constraint,('A','D'):maps_constraint, \
('D','F'):maps_constraint,('F','C'):maps_constraint,('C','B'):maps_constraint, \
('B','E'):maps_constraint,('C','E'):maps_constraint,('D','E'):maps_constraint, ('F','E'):maps_constraint}

colors = [1,2,3,4,5,6,7,8,9,10]
domains = { l:colors for l in ['A','B','C','D','E','F'] }

cs = ConstraintSearch(domains,cg)

#print(cs.search())

# 4 c)

cg = {('A','B'):maps_constraint,('A','F'):maps_constraint,('A','E'):maps_constraint, \
('A','D'):maps_constraint,('C','B'):maps_constraint,('F','C'):maps_constraint,('C','G'):maps_constraint, \
('C','D'):maps_constraint,('F','B'):maps_constraint,('F','G'):maps_constraint, ('F','E'):maps_constraint, \
('G','D'):maps_constraint,('G','E'):maps_constraint,('E','D'):maps_constraint,}

colors = [1,2,3,4,5,6,7,8,9,10]
domains = { l:colors for l in ['A','B','C','D','E','F','G'] }

cs = ConstraintSearch(domains,cg)

#print(cs.search())

'''

Domínio:
Mapa 1: Cores
Mapa 2: Cores
...

Grafo de Restrições:
Mapas adjacentes

'''
