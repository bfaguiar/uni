from constraintsearch import *

def friends_constraint(f1, c1, f2, c2):

	if c1[3]=="c" and c1[1]!="b":
		return False

	if c2[3]=="c" and c2[1]!="b":
		return False

	if c1[1]==c2[1]:
		return False

	if c1[3]==c2[3]:
		return False

	return True


pessoas = ["bernardo","claudio","andre"]

def make_constraint_graph(friends):
	return {(p,p2):friends_constraint for p in friends for p2 in friends if p!=p2}

def make_domains(friends):
	material = ["b"+nome1+"c"+nome2 for nome1 in ["a","b","c"] for nome2 in ["a","b","c"] if nome1!=nome2]
	return {p:[m for m in material if m[1]!=p[0] and m[3]!=p[0]] for p in friends}

cs = ConstraintSearch(make_domains(pessoas),make_constraint_graph(pessoas))

print(cs.search())

'''
Dominio:
Andre: ["bbcc","bccb"]
Bernardo: ["bacb","bcca"]
Claudio: ["bacb","bbca"]

constraint_graph:
(Andre,Bernardo),(Andre,Claudio),
(Bernardo,Claudio)

'''
