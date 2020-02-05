from constraintsearch import *

vars = ['A','B','C','D','E']
colors = ['verde','vermelho','azul']
domains = { v:colors for v in vars }

edges = [ (v,'E') for v in vars if v!='E' ]
edges+= [ ('A','B'),('A','D'),('C','D'),('C','B')]
edges+= [ (v2,v1) for (v1,v2) in edges ]

constraints = { e:(lambda v1,c1,v2,c2: c1!=c2) for e in edges}
print(constraints)
cs = ConstraintSearch(domains,constraints)

print(cs.search())
