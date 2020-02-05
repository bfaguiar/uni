def head(lst):
    if lst == []:
        return None
    return lst[0]


def tail(lst):
    if lst == []:
        return None
    if len(lst) == 1:
        return []
    return [lst[-1]] + tail(lst[:-1])


def pairs(lst1, lst2):
    if lst1 == []:
        return []
    if lst2 == []:
        return []
    return [([lst1[0]], [lst2[0]])] + pairs(lst1[1:], lst2[1:])


def menor(lst):
    if lst == []:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        rest = menor(lst[1:])
        min = lst[0]
        if rest < min:
            min = rest
        return min


##
def menorLista(lst):
    if lst == []:
        return None
    if len(lst) == 1:
        return (lst[0], [lst[0]])
    else:
        rest = menor(lst[1:])
        min = lst[0]
        if rest < min:
            min = rest
        return (min, lst[1:])


def menorMaior(lst):
    if lst == []:
        return None
    if len(lst) == 1:
        return (lst[0], lst[0])
    else:
        rest = menorMaior(lst[1:])
        min = lst[0]
        max = lst[0]
        if rest[0] < min:
            min = rest[0]
        if rest[1] > max:
            max = rest[1]
        return (min, max)
