import math
from functools import reduce

#1
odd = lambda x: x % 2 != 0

#2
positive = lambda x: x > 0

#3
lessthan = lambda x,y: x < y

#4
coordinates = lambda x,y: (math.sqrt(x**2+y**2),math.atan(x/y))

#5
func1 = lambda f,g,h: lambda x,y,z: h(f(x,y),g(y,z))

#6
def universal(lst, f):
    if lst==[]:
        return None
    if len(lst) == 1:
        return f(lst[0])
    return f(lst[0]) and universal(lst[1:],f)

#6 com map reduce
def univ(lst,b):
    return reduce(lambda r,x: r and b(x), lst,True)

#7
def existencial(lst, f):
    if lst==[]:
        return None
    if len(lst) == 1:
        return f(lst[0])
    return f(lst[0]) or existencial(lst[1:],f)


#9
def menor(lst, f):
    if lst == []:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        rest = menor(lst[1:],f)
        min = lst[0]
        if f(rest,min):
            min = rest
        return min


#12
def polares(lst):
    if lst == []:
        return []
    return [coordinates(lst[0][0], lst[0][1])] + polares(lst[1:])

#15
def apl(pair, f):
    if pair[0] == [] or pair[1] == []:
        return []
    return [(f(pair[0][0]),f(pair[1][0]))] + apl((pair[0][1:],pair[1][1:]), f)


