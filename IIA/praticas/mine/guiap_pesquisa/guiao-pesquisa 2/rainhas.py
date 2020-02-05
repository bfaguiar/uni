
from constraintsearch import *
from pprint import pprint

def queen_constraint(r1,c1,r2,c2):
    l1 = int(r1[1:]) # R1 -> 1
    l2 = int(r2[1:]) #R2 -> 2
    if c1==c2:
        return False
    if abs(l1-l2)==abs(c1-c2):
        return False
    return True

def make_constraint_graph(n):
    queens = [ 'R'+str(i+1) for i in range(n) ]
    ola = { (X,Y):queen_constraint for X in queens for Y in queens if X!=Y }
    #pprint(ola)
    return ola
    '''
    {
        ('R1', 'R2'): 
        ('R1', 'R3'): 

        ('R1', 'R4'): 
        ('R2', 'R1'): <function queen_constraint at 0x105042b00>,
        ('R2', 'R3'): <function queen_constraint at 0x105042b00>,
        ('R2', 'R4'): <function queen_constraint at 0x105042b00>,
        ('R3', 'R1'): <function queen_constraint at 0x105042b00>,
        ('R3', 'R2'): <function queen_constraint at 0x105042b00>,
        ('R3', 'R4'): <function queen_constraint at 0x105042b00>,
        ('R4', 'R1'): <function queen_constraint at 0x105042b00>,
        ('R4', 'R2'): <function queen_constraint at 0x105042b00>,
        ('R4', 'R3'): <function queen_constraint at 0x105042b00>}
 '''


def make_domains(n):
    queens = [ 'R'+str(i+1) for i in range(n) ] # R1, #R2, #r3, #r4
    cols = [ i+1 for i in range(n) ] # [1, 2, 3, 4]
    return { r:cols for r in queens }
    # {
    #   R1: {1, 2, 3, 4}
    #   R2: {1, 2, 3, 4}
    #   R3: {1, 2, 3, 4}
    #   R4: {1, 2, 3, 4}
    # } 

    # cada uma só pode estar em apenas uma coluna dif erent e . então  mete se  1 .. .4  
    # as rows ou linhas (c ) teem que ser neste caso o numero depois do Rs.,,.


cs = ConstraintSearch(make_domains(4),make_constraint_graph(4))

print(cs.search()) 

