def length(lst):
    if lst == []:
        return 0
    return length(lst[1:]) + 1


def sum(lst):
    if lst == []:
        return 0
    return sum(lst[1:] + lst[0])


def contains(lst, elem):
    if lst == []:
        return False
    if lst[0] == elem:
        return True
    return contains(lst[1:], elem)


def concatenate(lst1, lst2):
    if lst1 == []:
        return lst2
    tmp = concatenate(lst1[1:], lst2)
    tmp[0:0] = [lst1[0]]
    return tmp


def invert(lst):
    if lst == []:
        return []
    return invert(lst[1:]) + [lst[0]]


def capicua(lst):
    if lst == []:
        return True
    if lst[0] != lst[-1]:
        return False
    return capicua(lst[1:-1])


def replace(lst,x,y):
    if lst == []:
        return []
    tmp = replace(lst[1:], x, y)
    if lst[0] == x:
        tmp[0:0] = [y]
    else:
        tmp[0:0] = [lst[0]]
    return tmp
