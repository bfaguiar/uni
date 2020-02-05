def comprimento(lista):
    if lista == []:
        return 0

    return 1 + comprimento(lista[1:])

def soma(lista):
    if lista == []:
        return 0

    return lista[0] + soma(lista[1:])


def existe(lista, elem):
    if lista == []:
        return False

    return elem == lista[0] or existe(lista[1:], elem)

def concat(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1

    l1.append(l2[0])
    return concat(l1, l2[1:])
  
def capicua(lista):
    if lista == []:
        return True

    return lista[0] == lista[-1] and capicua(lista[1:-1])

def separar(lista):
    if lista == []:
        return [], []

    a1, b1 = lista[0]

    l1, l2 = separar(lista[1:])

    return [a1] + l1, [b1] + l2
  
def remove_e_conta(lista, elem):
    if lista == []:
        return lista, 0

    l, c = remove_e_conta(lista[1:], elem)

    if lista[0] == elem:
        return l, c+1
    else:
        return [lista[0]] + l, c

def cabeca(lista):
    if lista == []:
        return None
    return lista[0]
  
def cauda(lista):
    if lista == []:
        return None

    return lista[1:]

def juntar(l1, l2):
    if len(l1) != len(l2):
        return None

    if l1 == []:
        return []

    return [(l1[0], l2[0])] + juntar(l1[1:], l2[1:])
  
def menor(lista):
    if lista == []:
        return None

    m = menor(lista[1:])
    if m == None or lista[0] < m:
        return lista[0]
    return m
  
def max_min(lista):
    if lista == []:
        return None, None

    mx, mn = max_min(lista[1:])
    if mx, mn == None, None:
        return lista[0], lista[0]
    if lista[0] > mx:
        return lista[0], mn
    if lista[0] < mn:
        return mx, lista[0]:
    return mx, mn

l1 = [1,2,3,4,5]
l2 = ['a', 'b', 'c']
l3 = [(1, 'a'), (2, 'b'), (3, 'c')]
l4 = [1,3,4,5,6,1,2,3]
print(comprimento(l1))
print(soma(l1))
print(existe(l1, 5))
print(existe(l1, 6))
print(concat(l1, l2))
print(inverte(l1))
print(capicua([1,2,3]))
print(capicua([1,2,1]))
print(capicua([1,1]))
print(separar(l3))
print(remove_e_conta(l4, 1))
print(juntar(*separar(l3)))


l1 = [1,2,3,4,5]
l2 = ['a', 'b', 'c']
l3 = [(1, 'a'), (2, 'b'), (3, 'c')]
l4 = [1,3,4,5,6,1,2,3]
print(comprimento(l1))
print(soma(l1))
print(existe(l1, 5))
print(existe(l1, 6))
print(concat(l1, l2))
print(inverte(l1))
print(capicua([1,2,3]))
print(capicua([1,2,1]))
print(capicua([1,1]))
print(separar(l3))
print(remove_e_conta(l4, 1))
print(juntar(*separar(l3)))