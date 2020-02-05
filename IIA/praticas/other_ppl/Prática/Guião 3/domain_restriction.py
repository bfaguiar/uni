from constraintsearch import *

digits = list(range(0,10))

def generate_product_domain(lvars, domains):
	if lvars==[]:
		return[[]]

	product = generate_product_domain(lvars[1:], domains)
	final_product = []

	for v in domains[lvars[0]]:
		for x in product:
			newx = [v]+x
			final_product += [newx]

	return final_product


domains = { D:digits for D in ['O','R','T','U','W'] }
domains['F']  = [0,1]
domains['X1'] = [0,1]
domains['X2'] = [0,1]

def filter_domain(crossproduct, constraint):
	return [v for v in crossproduct if constraint(v)]

def all_different(Aux1):
    return len(set(Aux1)) == len(Aux1)

def orx1(Aux2):
    return 2*Aux2[0] == Aux2[1]+10*Aux2[2]

def wx1ux2(Aux3):
    return 2*Aux3[0]+Aux3[1] == Aux3[2]+10*Aux3[3]

def tx2of(Aux4):
    return 2*Aux4[0]+Aux4[1] == Aux4[2]+10*Aux4[3]

domains['FORTUW'] = generate_product_domain(['F','O','R','T','U','W'],domains)
domains['FORTUW'] = filter_domain(domains['FORTUW'],all_different)

domains['ORX1'] = generate_product_domain(['O','R','X1'],domains)
domains['ORX1'] = filter_domain(domains['ORX1'],orx1)

domains['WX1UX2'] = generate_product_domain(['W','X1','U','X2'],domains)
domains['WX1UX2'] = filter_domain(domains['WX1UX2'],wx1ux2)

domains['TX2OF'] = generate_product_domain(['T','X2','O','F'],domains)
domains['TX2OF'] = filter_domain(domains['TX2OF'],wx1ux2)


constraints = []

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[0]) 
    for edge in [('F','FORTUW'),('O','ORX1'),('W','WX1UX2'),('T','TX2OF')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[0]) 
    for edge in [('FORTUW','F'),('ORX1','O'),('WX1UX2','W'),('TX2OF','T')] ]

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[1]) 
    for edge in [('O','FORTUW'),('R','ORX1'),('X1','WX1UX2'),('X2','TX2OF')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[1]) 
    for edge in [('FORTUW','O'),('ORX1','R'),('WX1UX2','X1'),('TX2OF','X2')] ]

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[2]) 
    for edge in [('R','FORTUW'),('X1','ORX1'),('U','WX1UX2'),('O','TX2OF')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[2]) 
    for edge in [('FORTUW','R'),('ORX1','X1'),('WX1UX2','U'),('TX2OF','O')] ]

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[3]) 
    for edge in [('T','FORTUW'),('X2','WX1UX2'),('F','TX2OF')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[3]) 
    for edge in [('FORTUW','T'),('WX1UX2','X2'),('TX2OF','F')] ]

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[4]) 
    for edge in [('U','FORTUW')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[4]) 
    for edge in [('FORTUW','U')] ]

constraints += [ (edge,lambda var,val,auxvar,auxval : val==auxval[5]) 
    for edge in [('W','FORTUW')] ]
constraints += [ (edge,lambda auxvar,auxval,var,val : val==auxval[5]) 
    for edge in [('FORTUW','W')] ]


'''

digit_v = ['F','O','R','T','U','W']
carry_v = ['X1','X2']
aux_v = ['Aux1','Aux2','Aux3','Aux4']
variables = digit_v+carry_v+aux_v

digits = list(range(0,10))

domains = {d:digits for d in digit_v}
domains['X1'] = [0,1]
domains['X2'] = [0,1]

def generate_product_domain(lvars, domains):
	if lvars==[]:
		return[[]]

	product = generate_product_domain(lvars[1:], domains)
	final_product = []

	for v in domains[lvars[0]]:
		for x in product:
			newx = [v]+x
			final_product += [newx]

	return final_product

def all_different(Aux1):
	return len(set(Aux1))==len(Aux1)

def orx1(Aux2):
	return 2*Aux2[0]==Aux2[1]+10*Aux2[2]

def wx1u2(Aux3):
	return 2*Aux3[0]+Aux3[1]==Aux3[2]+10*Aux3[3]

def ax2pl(Aux4):
	return 2*Aux4[0]+Aux4[1]==Aux4[2]+10*Aux4[3]

def filter_product_domain(crossproduct, constraint):
	return [v for v in crossproduct if constraint(v)]

def aux(o, vo, aux2, vaux):
	if o=='F':
		return vo==vaux[0]
	elif o=='O':
		return vo==vaux[1]
	elif o=='R':
		return vo==vaux[2]
	elif o=='T':
		return vo==vaux[3]
	elif o=='U':
		return vo==vaux[4]
	elif o=='W':
		return vo==vaux[5]

	return False

def aux2(o, vo, aux2, vaux2):
	if o=='O':
		return vo==vaux2[0]
	elif o=='R':
		return vo==vaux[1]
	elif o=='X1':
		return vo==vaux[2]

	return False

def aux3(o, vo, aux3, vaux3):
	if o=='W':
		return vo==vaux3[0]
	elif o=='X1':
		return vo==vaux3[1]
	elif o=='U':
		return vo==vaux3[2]
	elif o=='X2':
		return vo==vaux3[3]

	return False

def aux4(o, vo, aux4, vaux4):
	if o=='T':
		return vo==vaux4[0]
	elif o=='X2':
		return vo==vaux4[1]
	elif o=='O':
		return vo==vaux4[2]
	elif o=='F':
		return vo==vaux4[3]
	return False

cross_aux1 = generate_product_domain(digit_v, domains)
domains['Aux1'] = filter_product_domain(cross_aux1, all_different)

cross_aux2 = generate_product_domain(['O','R','X1'], domains)
domains['Aux2'] = filter_product_domain(cross_aux2, orx1)

cross_aux3 = generate_product_domain(['W','X1','U','X2'], domains)
domains['Aux3'] = filter_product_domain(cross_aux3, wx1u2)

cross_aux4 = generate_product_domain(['T','X2','O','F'], domains)
domains['Aux4'] = filter_product_domain(cross_aux4, ax2pl)

constraintgraph = { ('O','Aux1'): aux, ('F','Aux1'): aux, ('R','Aux1'): aux,\
					('T','Aux1'): aux, ('U','Aux1'): aux, ('W','Aux1'): aux,\
					('O','Aux2'): aux2, ('R','Aux2'): aux2, ('X1','Aux2'): aux2,\
					('W','Aux3'): aux3, ('X1','Aux3'): aux3, ('U','Aux3'): aux3,\
					('X2','Aux3'): aux3, ('T','Aux4'): aux4, ('X2','Aux4'): aux4,\
					('O','Aux4'): aux4, ('F','Aux4'): aux4}

cs = ConstraintSearch(domains,constraintgraph)

'''