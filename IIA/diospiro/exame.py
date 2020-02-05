def interpretacoes(list):
	if list==[]:
		return [[]]

	rec = interpretacoes(list[1:])
	fin_list = []
	for el in rec:
		fin_list += [el+[(list[0],True)]]
		fin_list += [el+[(list[0],False)]]

	return fin_list

print interpretacoes(["a","b"])

def provar(list, var):
	var_list = [ ele for ele in list if ele[1]==var ]

	if var_list==[]:
		return None

	return any([all([provar(list, el) for el in v[0]]) for v in var_list])

print provar([([],"a"),([],"b"),(["a","b"],"c")],"c")


def add(nodes, newnodes):
	nodes.extend(newnodes)

