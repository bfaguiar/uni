#lambda functions

import math 
num_int_impar = lambda n: n % 2 == 1
positivo = lambda n: n >= 0
cart2polar = lambda x, y: (math.hypot(x, y), math.atan2(x, y))
exe4_5 = lambda f, g, h: lambda x, y, z: h(f(x,y), g(x,z))

def quantificador_universial(lista, f):
    return not False in [ f(e) for e in lista ]
    #return lista == [ e for e in lista if f(e) ]
    #return [] == [ e for e in lista if not f(e) ]

def quantificador_existencial(lista, f):
    return True in [f(e) for e in lista]

def menor_elem(lista, f):
    if len(lista) == 1:
        return lista[0]
    m = menor_elem(lista[1:], f)
    if f(lista[0], m):
        return lista[0]
    return m

def menor_e_remove(lista, f):
    if len(lista) == 1:
        return lista[0], []
    menor, lista = menor_e_remove(lista[1:], f)
    if f(lista[0], menor):
        return lista[0], [menor] + lista
    return menor, [lista[0]] + lista




print(num_int_impar(3))
print(positivo(4))
nova = exe4_5(lambda x,y: x+y, lambda x,y: x*y, lambda x,y: x<y)
print(nova(4, 1, 6))
print(quantificador_universial([1, 2, 3, 4, 5], lambda f: f < 5))
print(quantificador_existencial([1, 2, 3, 4], lambda f: f < 3))
print(menor_elem([1, 2, 3, 4, 5], lambda f, z: f < z))
print(menor_e_remove([4, 3, 2, 1], lambda f, z: f < z))

#= 0 == Truexnmenor = lem_lista
#gerador de listas:
# e for e in [1, 2, 3]
#output: gera uma lista, neste caso de [1, 2, 3]
