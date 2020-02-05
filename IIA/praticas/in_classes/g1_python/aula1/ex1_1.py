#1 Funções para processamento de listas
def comprimento(lista):
    if lista == []:
        return 0
    return 1 + comprimento(lista[1:])

def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

def existe(lista, n):
    if lista == []:
        return False
    if lista[0] == n:
        return True
    return existe(lista[1:], n)

def concat(lista1, lista2):
    if lista1 == []:
        return lista2
    if lista2 == []:
        return lista1
    lista1.append(lista2[0])
    return concat(lista1, lista2[1:])

def reverse(lista):
    if lista == []:
        return []
    return reverse(lista[1:]) + [lista[0]]

def capicua(lista):
    if lista == [] or len(lista) == 1:
        return True
     
    return lista[0] == lista[-1] and capicua(lista[1:-1])


#print(comprimento([1, 2, 3, 4]))
#print(soma([1, 2, 3, 4]))
#print(existe([1, 2, 3, 4], 2))
#print(concat([1, 2, 3, 4], [5, 6, 7, 8]))
#print(reverse([1, 2, 3, 4]))
print(capicua([1, 2, 3]))
print(capicua([1, 2, 1]))

''' 2: Fun ̧c ̃oes para processamento de listas e tuplos '''

def separar(lista):
    if lista == []:
        return ([], []) # retorna um
    a1, b1 = lista[0]
    lista1, lista2 = separar(lista[1:])
    return [a1] + lista1, [b1] + lista2

#def remove_e_conta(lista, n):
   # if lista == []:


# 3: Fucnoes que retornan None: None nao é zero. nem False, é ~e uma maneira de gerar uma excepcao. '''''' de

def cabeca(lista):
    if lista == []:
        return None
    return lista[0]

def cauda(lista):
    if lista == []:
        return None
    return lista[1:]

#def juntar(lista1, lista2):
 #   if len(lista1) != len(lista2):
 #       return None
 #  [ (lista1[0], lista2[0]) ] + juntar(lista2[1:], lista2[2:])

 #def menor(lista):
 #   if lista == []:
 #       return None
 #   m = menor(lista[1:])
 #   if m == None or lista

def maxmin(lista):
    if lista == []:
        return None
    return maxmin(lista[1:])


#print(separar([1, 2, 3, 4]))
print(cauda([1, 2, 3, 4]))
print()