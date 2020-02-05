# processamento listas

import math 

def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)
#print(factorial(5))

def length(lista):
    if lista == []: return 0
    return 1 + length(lista[1:])

def soma(lista):
    if lista == []: return 0
    return lista[0] + soma(lista[1:])

def ocorre(lista, n):
    if lista == []: return False 
    if lista[0] == n: return True
    return ocorre(lista[1:], n)

def concatenacao(lista1, lista23):
    if lista1 == []: return lista23
    if lista23 == []: return lista1
    lista1.append(lista23[0])
    return concatenacao(lista1, lista23[1:])

def inversaa(lista1):
    if lista1 == []: return []
    return  inversaa(lista1[1:]) + [lista1[0]] 

    #ou #return [lista1[0], lista23[0]] + concatenacao(lista1[1:], lista23[1:])

def capi(lista): #dificil
    if lista == []: return True
    return lista[0] == lista[-1] and capi(lista[1:-1])

def cat_lista(lista):
    if lista == []: return []
    return lista[0] + cat_lista(lista[1:])

def replace(lista, x, y):
    if lista == []: return []
    if lista[0] == x:
        return [y] + replace(lista[1:], x, y)
    return [lista[0]] + replace(lista[1:],x , y)

def uniaoordenada(lista1, lista2):
    if lista1 == []: return lista2
    if lista2 == []: return lista1
    if lista1[0] < lista2[0]: return [lista1[0]] + uniaoordenada(lista1[1:], lista2)
    return [lista2[0]] + uniaoordenada(lista1, lista2[1:])

'''
def ordered_union(list_1, list_2):
	if list_1 == [] and list_2 == []:
		return []
	elif list_2 == []:
		return list_1
	elif list_1 == []:
		return list_2
	elif list_2[0]<list_1[0]:
		return [list_2[0]]+ordered_union(list_1,list_2[1:])
	else:ordered_union
		return [list_1[0]]+ordered_union(list_1[1:],list_2)x
'''
def subsets(lista):
    if lista == []:
        return [[]]
    return [[lista[0]] + e for e in subsets(lista[1:])] + subsets(lista[1:]) # estou a encaixar os o primeiro elemento nos subsets ja criados + esses subsets. 
    #it2 [[3] + []] + [[]] = [[3], []]
    #it1 [[2] + [3], [2] + []] + it0 = [[2, 3], [2], [3], []]
    #it0 [[1] + [2, 3], [1] + [2], [1] + [3], [1] ] + it1 = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]


#processamento listas e tuplos

def separar_pares(lista):
    if lista == []: return [], []
    a, b = lista[0]
    l, m = separar_pares(lista[1:])
    return [a] + l, [b] +  m

def remove_e_conta(lista, elem):
    if lista == []: return [], 0
    listex, counter = remove_e_conta(lista[1:], elem)
    if lista[0] == elem: return listex, 1 + counter
    return [lista[0]] + listex, counter

def total_elem_ocorre(lista):
    if lista == []: return {}
    if len(lista) == 1: return {lista[0]:1}
    listex= total_elem_ocorre(lista[1:])
    
    if lista[0] in listex: listex[lista[0]]+=1
    else: listex[lista[0]] = 1
    return listex

#Funcoes que retornan None

def elem_cabeca(lista):
    if lista == []: return None
    else: return lista[0]

def elem_cauda(lista):
    if lista == []: return None
    if len(lista) == 1: return lista
    return elem_cauda(lista[1:])

def juntam(lista, lista2):
    if lista == []: return []
    if len(lista) != len(lista2): return None
    return [(lista[0], lista2[0])] + juntam(lista[1:], lista2[1:])

def menor(lista):
    if lista == []: return None
    m = menor(lista[1:])
    if m == None or lista[0] < m:
        return lista[0]
    return m

def menor_par(lista):
    if lista == []: return None, []
    if len(lista) == 1:
        return lista[0], []
    m, lista_aux = menor_par(lista[1:])
    if lista[0] < m:
        return lista[0], [m] + lista_aux # porque no final faz: [2] + [], depois [9] + [2], etc...
    return m, [lista[0]] + lista_aux

def max_min(lista):
    if len(lista) == 1: return lista[0], lista[0]
    if lista == []: return None, None
    max, min = max_min(lista[1:])
    if (lista[0] < min):
        return max, lista[0]
    elif (lista[0] > max):
        return lista[0], min
    else:
        return max, min 

def dois_menores(lista): 
    if len(lista) == 1: return lista[0], lista[0], [lista[0]]
    if lista == []: return None, None, []
    min1, min2, lista_aux = dois_menores(lista[1:])
   # if min1 == None or min2 == None: return lista[0], lista[0], [] Incorrecto, tenho que retoirnar
    if (lista[0] < min1): return lista[0], min2, [min2] + lista_aux
    if (lista[0] < min2): return min1, lista[0], [min1] + lista_aux
    return min1, min2, [lista[0]] + lista_aux

#Expressoes lambda:

n_inteiro = lambda n: n % 2 != 0
coordenadas = lambda x, y: (math.hypot(x, y), math.atan2(y,x ) )
funcao = lambda f, g, h: lambda x, y, z: h(f(x, y), g(y, z))

def quanitificador_universal(lista, f):

    return not False in [f(x) for x in lista]

def funcao_hunaria(f, g):
    return True in [g(x) for x in f]

def a(self, parameter_list):
    pass 

def _2lists(lista1, lista3):
    return not False in [e1 == e for e1, e in zip(lista1, lista3)]

def reduce1(lista, f, neutro):
    if lista == []: return neutro
    return f(lista[0], reduce1(lista[1:], f, neutro))

def map(lista, f, neutro):
    if lista == []: return []
    if f(lista[0]): 
        return [lista[0]] + map(lista[1:], f, neutro)
    return map(lista[1:], f, neutro)


def min_list(lista, f): 
    return reduce1(lista, f, 1000), [l for l in lista if l != reduce1(lista, f, 1000)]

def min2_list(lista, f):
    if len(lista) < 2: return None, None, []
    return reduce1(lista, f, 1000)

# Algoritmos de selection e sort


def selectionSort(lista):
    if lista == []: return []
    menor = reduce1(lista, lambda x, y: x if x < y else y, 100000)
    index_menor = lista.index(menor)
    lista[index_menor] = lista[0]   # caso o index esteja numa posicao diferente de zero tem que se o meter em zero.
    lista[0] = lista[index_menor]
    return [menor] + selectionSort(lista[1:])


def BubbleSort(lista):
    if lista == []: return []
    maior = reduce1(lista, lambda x, y: x if x > y else y, 10000000)
    index_maior = lista.index(maior)
    lista[index_maior] = lista[-1]
    lista[-1] = lista[index_maior]
    return BubbleSort(lista[:-1]) + [maior]


lista_1 = [1, 2, 3, 4]
lista_3 = [1,4]
lista_4 = [1, 2]
listaa_aa1 = [1, 2, 7, 5, 9, 0, 1]
lista_2 = [0, 0]
lista5 = [0, 0,1]
lista= [1, 1, 2, 3, 4]
listaa = [0, 1, 2, 3, 4]
listaa_a = [-1, 2, 3, 4, 5]
listaa_aa = [-4, -3, -2, -1, 0]

#print(selectionSort(listaa_aa1))
#print(BubbleSort(listaa_aa1))

#menor_element = reduce1(lista_1, lambda x, y: x if x < y else y, 100000)
#print(menor_element)
#min_lista = min_list(lista_1, lambda x, y: x if x < y else y)
#print(min_lista)
#print(_2lists(lista_1, lista_3))
#print(_2lists)

#print(n_inteiro(3))
#nova = funcao(lambda x, y: x+y, lambda x, y: x*y, lambda x, y: x**y)
#print(nova(4, 1, 2)) 
func = 0
#print(quanitificador_universal(listaa_aa, lambda l: l < 0 ))  
#print(funcao_hunaria(listaa_aa, lambda x: x < 0))



#print(max_min(lista))
#lista2= [3, 4, 7, 9, 1, 2]
#print(dois_menores(lista2))
#print(menor_par(lista2))
#lista1= [1, 2, 3, 4, 5, 6]
#lista2 = [2, 2, 3, 4, 8, 9, 10]
#lista23=[1, 2, 3, 5] 
#lista32=[1,2,1]
#lista332=[1,2,3,3,2,1]
#listaa_2=[[123], [1, 2, 3], [1, 2], [4, 5]]
#lista_pares = [(1, 2), (2, 3), (5, 6), (7, 8)]
#print(menor(lista))
#print(length(lista))#ull
print(soma(lista))
#print(ocorre(lista, 5))[]
#listex = concatenacao(lista, lista23)s 
#print(listex)s
#print(contagem(lista))
#print(inversaa(lista))
#print(capi(lista))
#print(capi(lista23))
#print(capi(lista32))
#print(capi(lista332))
#print(cat_lista(listaa_2))
#print(replace(lista, 2, 3))
#print(uniaoordenada(lista1, lista2))
#print(subsets(lista))
#print(separar_pares(lista_pares))
#print(remove_e_conta([2, 2, 2, 3], 2))

#print(total_elem_ocorre(lista))


#8m#ne[]for e in, o # incorrecto duvida#incorrecto duvida#2134 4))))(cuaand1[]=+ lista[1] lista[0] +  lista_return = [] lista_return.append(lista[0])andlista_returnremove_e_conta(lista[1:], elem)))[], 0,  s


# lixo

#reduce
#idk why

   # mm = reduce(lista[1:], f, neutro)
'''
    if lista == []: return None, []
    if len(lista) == 1: return lista[0], [lista[0]]
    inteiro, lista = min_list(lista[1:], f)
    if (f(lista[0], inteiro)):
        return lista[0], [inteiro] + lista
    return inteiro, [lista[0]] + lista 

''' 