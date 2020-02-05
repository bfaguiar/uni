#
# Modulo: cidades
# 
# Implementacao de um dominio para planeamento de caminhos
# entre cidades usando para esse efeito o modulo tree_search
#
# (c) Luis Seabra Lopes, Introducao a Inteligencia Artificial, 2012/2013
#


from tpi2 import *
from math import *

class Cidades(SearchDomain):
    def __init__(self,connections, coordinates):
        self.connections = connections
        self.coordinates = coordinates
    def actions(self,Cidade):
        actlist = []
        for (C1,C2,D) in self.connections:
            if (C1==Cidade):
                actlist += [(C1,C2)]
            elif (C2==Cidade):
               actlist += [(C2,C1)]
        return actlist 
    def result(self,state,action):
        (C1,C2) = action
        if C1==state:
            return C2
    def cost(self,state,action):
        (c1,c2) = action
        if c1!=state:
            return None
        for (x,y,d) in self.connections:
            if ( (x==c1 and y==c2) or (x==c2 and y==c1) ):
                return d
    def heuristic(self,state,goal):
        (x1,y1) = self.coordinates[state]
        (x2,y2) = self.coordinates[goal]
        return sqrt( (x1-x2)**2 + (y1-y2)**2 )


cidades_portugal = Cidades( 
                    # Ligacoes por estrada
                    [
                      ('Coimbra', 'Leiria', 73),
                      ('Aveiro', 'Agueda', 35),
                      ('Porto', 'Agueda', 79),
                      ('Agueda', 'Coimbra', 45),
                      ('Viseu', 'Agueda', 78),
                      ('Aveiro', 'Porto', 78),
                      ('Aveiro', 'Coimbra', 65),
                      ('Figueira', 'Aveiro', 77),
                      ('Braga', 'Porto', 57),
                      ('Viseu', 'Guarda', 75),
                      ('Viseu', 'Coimbra', 91),
                      ('Figueira', 'Coimbra', 52),
                      ('Guarda', 'Castelo Branco', 96),
                      ('Leiria', 'Castelo Branco', 169),
                      ('Figueira', 'Leiria', 62),
                      ('Leiria', 'Santarem', 78),
                      ('Santarem', 'Lisboa', 82),
                      ('Santarem', 'Castelo Branco', 160),
                      ('Castelo Branco', 'Viseu', 174),
                      ('Santarem', 'Evora', 122),
                      ('Lisboa', 'Evora', 132),
                      ('Lisboa', 'Setubal', 62),
                      ('Setubal', 'Beja', 100),
                      ('Evora', 'Beja', 80),
                      ('Lisboa', 'Beja', 178),
                      ('Faro', 'Beja', 147) ],

                    # Coordenadas das cidades:
                     { 'Aveiro': (41,215),
                       'Figueira': ( 24, 161),
                       'Coimbra': ( 60, 167),
                       'Agueda': ( 58, 208),
                       'Viseu': ( 104, 217),
                       'Braga': ( 61, 317),
                       'Porto': ( 45, 272),
                       'Lisboa': ( 0, 0),
                       'Santarem': ( 38, 59),
                       'Leiria': ( 28, 115),
                       'Castelo Branco': ( 140, 124),
                       'Guarda': ( 159, 204),
                       'Evora': (120, -10),
                       'Beja': (125, -110),
                       'Setubal': (0,-55),
                       'Faro': (120, -250)
                     } )


p = SearchProblem(cidades_portugal,'Lisboa','Faro')
t = MyTree(p,'depth')
print(t.search())
print(t.optimize())
print(t.optimizations)

p = SearchProblem(cidades_portugal,'Lisboa','Faro')
t = MyTree(p,'astar_limited',5000)
print(t.search2())
print(t.solution_cost)
print(t.solution_length)
print(t.tree_size)

t = MyTree(p,'astar_limited',290)
print(t.search2())
print(t.solution_cost)
print(t.solution_length)
print(t.tree_size)

# Atalho para obter caminho de c1 para c2 usando strategy:
def search_path(c1,c2,strategy):
    my_prob = SearchProblem(cidades_portugal,c1,c2)
    my_tree = SearchTree(my_prob)
    my_tree.strategy = strategy
    return my_tree.search()

