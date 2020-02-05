def membro(lista, x):
    if lista == []: return False
    return (lista[0] == x) or membro(lista, x)

def inverter(lista):
    if lista == []: return []
    return inverter(lista[1:]) + [lista[0]]
    
def inverter_prof(lista):
    if lista == []: return []
    inv = inverter(lista[1:])
    inv[len(inv):] = [lista[0]]
    return inv

def pesq_raiz(a, b, f, valor):
    mediana = (a+b)/2
    if (b-a) < valor:
        return mediana
    if f(mediana) * f(a) < 0:
        return pesq_raiz(a, mediana, f, valor)
    return pesq_raiz(mediana, b, f, valor)

def aplicar(lista, f): # corresponde ao map 
        if lista == []: return []
        return [f(lista[0])] + aplicar(lista[1:], f)
    
def reduzir(lista, f, valor_neutro):
    if lista == []: return valor_neutro
    
    return f(lista[0], reduzir(lista[1:], f, valor_neutro))


def filtrar(lista, f): # corresponde ao reduce
    if lista == []: return []
    if f(lista[0]): return [lista[0]] + filtrar(lista[1:], f)
    return filtrar(lista[1:], f)
    

    
'''
def filtrar(f,lista): 
    if lista==[]:
        return [] 
    if f(lista[0]):
        return [lista[0]] + filtrar(f,lista[1:]) 
    return filtrar(f,lista[1:])
''' 


print(filtrar)
#print(filtrar([2,-4,17], lambda x : x%2==0))
#print(filtrar(lambda x : x%2==0, [2,-4,17]))
print(aplicar([1, 2, 3, 4], lambda x: x**2))
lista = [1, 2, 3, 4, 5,6]
print(reduzir(lista, lambda x, y: x < y, -1)) 
print(inverter_prof(lista))#*
print(inverter(lista))
print(lista)
