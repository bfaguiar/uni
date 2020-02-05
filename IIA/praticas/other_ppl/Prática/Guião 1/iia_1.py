# Diogo Daniel Soares Ferreira
# IIA, 2016/2017
# diogodanielsoaresferreira@ua.pt
# Aula prática 1

###################################### I ##############################


def len_list(list_in):
	if list_in != []:
		return 1+len_list(list_in[1:])
	else:
		return 0

#print(len_list([1,2,3]))



def converte_inteiros(lista):
	if lista==[]:
		return []
	else:
		return [int(lista[0])]+converte_inteiros(lista[1:])

#print(converte_inteiros(['1','2','3']))



def sum_rec(list_num):
	if list_num!=[]:
		return list_num[0]+sum_rec(list_num[1:])
	else:
		return 0

#print(sum_rec([1,2,3]))



def is_in_list(list_in, elem):
	if list_in!=[]:
		if list_in[0]==elem:
			return True
		else:
			return is_in_list(list_in[1:], elem)
	else:
		return False

#print(is_in_list([1,2,3,4,5],4))
#print(is_in_list([1,2,3,4,5],6))



def conc_list(first_list, second_list):
	if first_list!=[]:
		return [first_list[0]]+conc_list(first_list[1:], second_list)
	if second_list!=[]:
		return [second_list[0]]+conc_list(first_list, second_list[1:])
	else:
		return []

#print(conc_list([1,2,3],[4,5,6,7]))



def reverse_list(list_in):
	if len(list_in)>1:
		return [list_in[-1]]+reverse_list(list_in[:-1])
	elif list_in!=[]:
		return [list_in[-1]]
	else:
		return []

#print(reverse_list([1,2,3,4,5,4,3,2,7]))



def capicua(list_in):
	if len(list_in)<2:
		return True
	elif list_in[0]!=list_in[-1]:
		return False
	else:
		return capicua(list_in[1:-1])

#print(capicua(['a','b','c','b','a']))



def conc_lists(lists):
	if lists==[]:
		return []
	else:
		return lists[0]+conc_lists(lists[1:])

#print(conc_lists([[1,2,3],[4,5,6],[7,8,9]]))



def substitute(list_in, x, y):
	if list_in==[]:
		return []
	elif list_in[0]==x:
		return [y]+substitute(list_in[1:],x,y)
	else:
		return [list_in[0]]+substitute(list_in[1:],x,y)

#print(substitute(['a','b','c','d','e'],'c','f'))



def ordered_union(list_1, list_2):
	if list_1 == [] and list_2 == []:
		return []
	elif list_2 == []:
		return list_1
	elif list_1 == []:
		return list_2
	elif list_2[0]<list_1[0]:
		return [list_2[0]]+ordered_union(list_1,list_2[1:])
	else:
		return [list_1[0]]+ordered_union(list_1[1:],list_2)

#print(ordered_union([2,3,5],[2,5,5]))


def subsets(list_in):
	if list_in==[]:
		return [[]]

	t = subsets(list_in[1:])
	return t+[[list_in[0]]+e for e in t]

#print(subsets([1,2,3,4,5]))


###################################### II ##############################

def two_lists(list_in):
	if list_in == []:
		return [],[]
	else:
		t1, t2 = list_in[0]
		l1, l2 = two_lists(list_in[1:])
		return [t1]+l1,[t2]+l2

#print(two_lists([(1,2),(3,4),(5,6),(7,8)]))



def remove_e_conta(list_in, x):
	if list_in == []:
		return [],0
	else:
		list_c, x_c = remove_e_conta(list_in[1:],x)
		if list_in[0]==x:
			return list_c, x_c+1
		else:
			return [list_in[0]]+list_c,x_c

#print(remove_e_conta([1,6,2,5,5,2,5,2],2))


def contagem(list_in):
	if list_in == []:
		return {}
	elif len(list_in)==1:
		return {list_in[0]:1}
	else:
		c = contagem(list_in[1:])
		if list_in[0] in c:
			c[list_in[0]]+=1
		else:
			c[list_in[0]]=1
		return c

#print(contagem([1,2,3,4,4,5,7,7,7,1]))


###################################### III ##############################

def cabeca(list_in):
	if list_in == []:
		return None
	else:
		return list_in[0]

#print(cabeca([1,2,3]))
#print(cabeca([]))


def cauda(list_in, estou_na_cauda=False):
	if list_in == []:
		return None
	elif len(list_in) == 1 and not estou_na_cauda:
		return []
	elif estou_na_cauda:
		c = cauda(list_in[1:], True)
		if c==None:
			return [list_in[0]]
		return [list_in[0]]+c
	else:
		return cauda(list_in[1:], True)

#print(cauda([1,2,3,4,5,1]))


def homologos(list_1, list_2):
	if list_1 == [] and list_2 == []:
		return None
	elif len(list_1) == 1:
		return [(list_1[0], list_2[0])]
	else:
		return [(list_1[0],list_2[0])]+homologos(list_1[1:], list_2[1:])

#print(homologos([1,2,3],[2,4,5]))


def minimum(list_in):
	if list_in == []:
		return None
	elif len(list_in)==1:
		return list_in[0]
	else:
		minim = minimum(list_in[1:])
		if minim<list_in[0]:
			return minim
		else:
			return list_in[0]

#print(minimum([1,6,2,9,-1,34,99,2,0]))


def min_all(list_in):
	if list_in == []:
		return None
	elif len(list_in) == 1:
		return (list_in[0],[])
	else:
		minim, left = min_all(list_in[1:])
		if minim>list_in[0]:
			return (list_in[0],left+[minim])
		else:
			return (minim, left+[list_in[0]])

#print(min_all([1,6,2,9,-1,34,99,2,0]))



def max_min(list_in):
	if list_in == []:
		return None
	elif len(list_in)==1:
		return(list_in[0], list_in[0])
	else:
		maxim, minim = max_min(list_in[1:])
		if list_in[0]>maxim:
			maxim = list_in[0]
		if list_in[0]<minim:
			minim = list_in[0]
		return (maxim, minim)

#print(max_min([1,5,9,2,7,-1,56,99,-1,3]))


def triple_min(list_in):
	if list_in == []:
		return None
	elif len(list_in) == 1:
		return (list_in[0], None ,[])
	elif len(list_in) == 2:
		if list_in[1]>list_in[0]:
			return (list_in[0],list_in[1],[])
		else:
			return (list_in[1],list_in[0],[])
	else:
		smallest, sec_smallest, left = triple_min(list_in[1:])
		if list_in[0]>sec_smallest:
			return (smallest, sec_smallest, left+[list_in[0]])
		elif list_in[0]<smallest:
			return (list_in[0], smallest, left+[sec_smallest])
		else:
			return (smallest, list_in[0], left+[sec_smallest])

#print (triple_min([1,5,9,2,7,-1,56,99,-1,3,-5]))

def media_mediana(list_in, i=0):
	if list_in == []:
		return None
	elif len(list_in)==1:
		return list_in[0],1
	elif i==0:
		media, all_elem = media_mediana(list_in[1:],i+1)
		return (list_in[0]+media)/(all_elem+1),list_in[(all_elem+1)//2]
	else:
		media, all_elem = media_mediana(list_in[1:],i+1)
		return list_in[0]+media,all_elem+1

print(media_mediana([2,2,2,3,3,3,4,4,4]))
