##################################

# PRODUCTO CARTESIANO DOS DOMINIOS:
def producto(listvars):
    if listvars == {}:
        return [()]
    prod = producto(listvars[1:].dominios)
    return [(x,)+ t for x in dominios(listvars[0] for t in prod)]

####################################### o que nos estamos aqui a fazer é gerar um dominio e um grafo para aplicar a tree_search.



variaveis = ["F", "O", "R", "T", "U", "W"]

algarismos = list(range(10))

dominios = { v:algarismos for v in variaveis } # todas as variaveis teem como dominio o conjunto dos algarismos.

dominios["X1"] = [0,1] # acrescentar a este dicionario, estas entradas
dominios["X2"] = [0,1] # igual.

# acrescentar ainda mais uma variavel
dominios["orx1"] = [ (o, r, x1) for (o, r, x1) in producto(['O', 'R', 'X1'].dominios) ]

# dominios["orx1"] = [ (o,r,x1) for o in dominios["o"] for r in dominios["r"] for x1 in dominios["X1"] if 2*o == r + 10*X1] # dominio sem pre processamento. xxxx 3 producto carteziano. dominio sao tuplos.

#dominios["WX1UX2"] = [ (w, x1, u, x2) for w in dominios["w"] for x1 in dominios["X1"] for u in dominios["X2"] if 2*w + x1 == u + 10*x2]

#dominios["2TX20F"] = [ (t, x2, o, f) for ... if 2*t + x2 == o +10*f]

def different(v1, x1, v2, x2):
    return x1 != x2

pares = [ (v1, v2) for v1 in variaveis for v2 in variaveis if v1 != v2]

grafo = {p:different for p in pares}

grafoaux = {}   
grafoaux[("o", "orx1")] = lambda o, oval, orx1, orx1val : orx1val[0] == o
#grafoaux[("ORX1", "o")] = ....

grafoaux[("X1", "ORX1")] = lambda x1, x1val, orx1, orx1val: orx1val[2] == x1
grafoaux[('R', 'ORX1')] = lambda r, rval, orx1, orx1val: orx1val[1] == r

arcos = grafoaux.keys()
grafoinv = { (v2, v1): lambda v2, x2, v1, x1 : grafoaux[(v1, v2)](v1, x1, v2, x2) for (v1, v2) in grafoaux }

#JUNTAR OS TRES DICIONARIOS AKA GRAFOS

#print(producto(['O', 'R', 'X1'].dominios))





