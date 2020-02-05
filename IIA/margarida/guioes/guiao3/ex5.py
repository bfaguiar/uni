from constraintsearch import *

a = [('ch_b','bic_c'), ('ch_c','bic_b')]
b = [('ch_a','bic_c'), ('ch_c','bic_a')]
c = [('ch_a','bic_b'), ('ch_b','bic_b')]

vars = ['A','B','C']
colors = ['verde','vermelho','azul']
domains = { v:colors for v in vars }

edges = [ (v,'E') for v in vars if v!='E' ]
edges+= [ ('A','B'),('A','D'),('C','D'),('C','B')]
edges+= [ (v2,v1) for (v1,v2) in edges ]

constraints = { e:(lambda v1,c1,v2,c2: c1!=c2) for e in edges}
cs = ConstraintSearch(domains,constraints)

print(cs.search())
