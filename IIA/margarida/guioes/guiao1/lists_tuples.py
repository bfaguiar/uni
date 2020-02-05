def separar(lst):
    if lst == []:
        return ([], [])
    tmp = separar(lst[1:])
    return ([lst[0][0] + tmp[0]], [lst[0][1] + tmp[1]])


def remove_e_conta(lst, x):
    if lst == []:
        return [], 0
    tmp, count = remove_e_conta(lst[1:],x)
    if lst[0] == x:
        return tmp, count+1
    return [lst[0]] + tmp,count


##
def contagem(lst):
    if lst == []:
        return []
    tmp = contagem(lst[1:])
    return [(lst[0], 1)] + contagem(lst[1:])
