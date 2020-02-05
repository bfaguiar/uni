# Diogo Daniel Soares Ferreira
# IIA, 2016/2017
# diogodanielsoaresferreira@ua.pt
# Aula pratica 2

import math
from functools import reduce

###################################### IV ##############################

impar = (lambda x: x%2==1)
#print(impar(1))

positive = (lambda x: x>0)
#print(positive(-1))

two_n = (lambda x,y: abs(x)<abs(y))
#print(two_n(2,2))

coor_polares = (lambda p: (math.sqrt(p[0]**2+p[1]**2),math.atan(p[1]/p[0])))
#print(coor_polares((45,45)))


#5
concat_func = lambda f,g,h: lambda x,y,z: h(f(x,y), g(y,z))
menor_que = lambda x,y: x if x<y else y
f = concat_func(menor_que,menor_que,menor_que)
#print(f(1,-3,5))


#6
#print(all(x==0 for x in [0,0,0,0,0]))

#7
#print(any(x==0 for x in [1,2,0,4,5]))

#8
#print(all(x==y for x,y in zip([1,2,3], [1,2,3])))
# ou
#all(elem for elem in [1,2,3] if elem in [4,5,2,3])


#9
#print(reduce(lambda x,y: y if x>y else x, [1,2,3,4,5,-1]))
#ou
def ex9(lst, b):
    return reduce(lambda m,x: m if b(m,x) else x, lst)

#print(ex9([1,2,6,9,-4],lambda x,y: x<y))


#10
def ex10(lista, f):
	return ex9(lista, f), [l for l in lista if l!= ex9(lista, f)]

#print(ex10([1,2,3,8,9,5],lambda x,y: x<y))

#11
def ex11(lista, f):
	m1, r = ex10(lista, f)
	m2, rr = ex10(r, f)
	return m1,m2, [l for l in lista if l not in [m1, m2]]
#print(ex11([1,2,3,4,5,-6],lambda x,y:x<y))

#12
f12 = map(lambda x: (math.sqrt(x[0]**2+x[1]**2),math.atan(x[1]/x[0])), [[45,45], [60,30], [30,60]])
#print(list(f12))


#13
def ex13(l1, l2, f):
	if l1==[] or l2==[]:
		return l1+l2
	if f(l1[0], l2[0]):
		return [l1[0]] + ex13(l1[1:], l2,f) 
	else:
		return [l2[0]] + ex13(l1, l2[1:],f)

l2 = [3,5,6,7,8,12,54]
l3 = [5,7,89,123,324,554]
#print(ex13(l2, l3, lambda x,y: x<y))

#14
func = lambda x:x**2
listas = [[1,2,3,4,5],[6,2,8,9,10]]

func_14 = reduce(lambda r,h: r+list(map(func,h)),listas,[])
#print(func_14)


#15
func = lambda x,y: x==y
func_15 = reduce(lambda r,h: r+[func(h[0],h[1])], zip(listas[0],listas[1]),[])
#print(func_15)


#16
func = lambda x:x+1
init = []
# Para cada lista, há um reduce
# Para cada reduce, há outro reduce
func_16 = reduce(lambda r,h: r+[reduce(lambda r,h: r+func(h),h)], listas, [])
#print(func_16)

################################# V ###############################

list_1 = [1,2,3,9,8,6,2,8]

def is_sorted(list_in):
	
	if list_in == []:
		return True

	elif len(list_in)<2:
		return True

	if list_in[0]>list_in[1]:
		return False

	return is_sorted(list_in[1:])


def selection_sort(list_in):

	if list_in == []:
		return []

	smallest = reduce(lambda x,y: x if x<y else y, list_in)

	smallest_idx = list_in.index(smallest)
	list_in[0], list_in[smallest_idx] = list_in[smallest_idx], list_in[0]
	return [list_in[0]]+selection_sort(list_in[1:])

#print(selection_sort(list_1))
#print(is_sorted(selection_sort(list_1)))
#print(list_1)
#print(is_sorted(list_1))


def bubble_sort(list_in):
	
	if is_sorted(list_in):
		return list_in

	list_in = list_in[:]

	for i in range(len(list_in)-1):
		if list_in[i]>list_in[i+1]:
			list_in[i+1], list_in[i] = list_in[i], list_in[i+1]

	return bubble_sort(list_in[:-1])+[list_in[-1]]


#print(bubble_sort(list_1))
#print(is_sorted(bubble_sort(list_1)))


def quick_sort(list_in):

	if len(list_in)<=1:
		return list_in

	pivot = list_in[0]

	prev = [p for p in list_in[1:] if p<pivot]
	nxt = [n for n in list_in[1:] if n >= pivot]

	return quick_sort(prev)+[pivot]+quick_sort(nxt)


#print(quick_sort(list_1))

relation = lambda x,y: True if x<=y else False


def is_sorted_2(list_in, relation):
	
	if list_in == []:
		return True

	elif len(list_in)<2:
		return True

	if not relation(list_in[0], list_in[1]):
		return False

	return is_sorted_2(list_in[1:], relation)


def selection_sort_2(list_in, relation):

	if list_in == []:
		return []

	smallest = reduce(lambda x,y: x if relation(x,y) else y, list_in)
	idx = list_in.index(smallest)
	list_in[0], list_in[idx] = list_in[idx], list_in[0]
	return [list_in[0]]+selection_sort_2(list_in[1:], relation)

#print(selection_sort_2(list_1, relation))


def bubble_sort2(list_in, relation):
	if is_sorted_2(list_in, relation):
		return list_in

	list_in = list_in[:]

	for i in range(len(list_in)-1):
		if not relation(list_in[i], list_in[i+1]):
			list_in[i], list_in[i+1] = list_in[i+1], list_in[i]

	return bubble_sort2(list_in[:-1], relation)+[list_in[-1]]

#print(bubble_sort2(list_1, relation))


def quick_sort2(relation, list_in):
	if len(list_in)<=1:
		return list_in

	pivot = list_in[0]

	prev = [p for p in list_in[1:] if relation(p,pivot)]
	nxt = [n for n in list_in[1:] if not relation(n,pivot)]

	return quick_sort(prev)+[pivot]+quick_sort(nxt)

#print(quick_sort2(relation, list_1))