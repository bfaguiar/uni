
import math
from tpi2 import *


# -------------------------------------------------------------
# Rede de Bayes para testes
# -------------------------------------------------------------

bn = MyBN()

bn.add('a',[],0.003)
bn.add('b_a',[],0.002)
bn.add('c_s',[('a',True )],0.48)
bn.add('c_s',[('a',False)],0.08)

bn.add('d',[],0.01)
bn.add('m_f',[],0.01)
bn.add('b_v',[('c_s',True ),('b_a',True )],0.18)
bn.add('b_v',[('c_s',True ),('b_a',False)],0.02)
bn.add('b_v',[('c_s',False),('b_a',True )],0.90)
bn.add('b_v',[('c_s',False),('b_a',False)],0.68)
bn.add('s_m',[],0.05)

bn.add('s_p',[],0.3)
bn.add('v_p',[('m_f',True),('d',True ),('b_v',True )],0.003)
bn.add('v_p',[('m_f',True),('d',True ),('b_v',False )],0.12)
bn.add('v_p',[('m_f',True),('d',False ),('b_v',True)],0.08)
bn.add('v_p',[('m_f',True),('d',False),('b_v',False )],0.01)
bn.add('v_p',[('m_f',False),('d',True),('b_v',True)],0.04)
bn.add('v_p',[('m_f',False),('d',True ),('b_v',False)],0.07)
bn.add('v_p',[('m_f',False),('d',False),('b_v',True )],0.13)
bn.add('v_p',[('m_f',False),('d',False),('b_v',False)],0.09)
bn.add('h',[('b_v',True )],0.44)
bn.add('h',[('b_v',False)],0.89)
bn.add('s_s',[('s_m',True),('m_f',True ),('b_v',True )],0.3)
bn.add('s_s',[('s_m',True),('m_f',True ),('b_v',False )],0.21)
bn.add('s_s',[('s_m',True),('m_f',False ),('b_v',True)],0.34)
bn.add('s_s',[('s_m',True),('m_f',False),('b_v',False )],0.12)
bn.add('s_s',[('s_m',False),('m_f',True),('b_v',True)],0.15)
bn.add('s_s',[('s_m',False),('m_f',True ),('b_v',False)],0.14)
bn.add('s_s',[('s_m',False),('m_f',False),('b_v',True )],0.132)
bn.add('s_s',[('s_m',False),('m_f',False),('b_v',False)],0.44)

bn.add('s_t',[('d',True )],0.08)
bn.add('s_t',[('d',False)],0.002)
bn.add('s_q',[('s_p',True ),('v_p',True )],0.008)
bn.add('s_q',[('s_p',True ),('v_p',False)],0.4)
bn.add('s_q',[('s_p',False),('v_p',True )],0.51)
bn.add('s_q',[('s_p',False),('v_p',False)],0.13)
bn.add('f_s',[],0.1)
bn.add('c_c',[('s_s',True )],0.49)
bn.add('c_c',[('s_s',False)],0.023)

bn.add('car_s',[('c_c',True),('s_t',True),('s_q',True ),('f_s',True )],0.091)
bn.add('car_s',[('c_c',True),('s_t',True),('s_q',True ),('f_s',False )],0.081)
bn.add('car_s',[('c_c',True),('s_t',True),('s_q',False ),('f_s',True )],0.045)
bn.add('car_s',[('c_c',True),('s_t',True),('s_q',False ),('f_s',False )],0.065)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',True ),('f_s',True)],0.087)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',True),('f_s',False )],0.043)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',False ),('f_s',True)],0.035)
bn.add('car_s',[('c_c',True),('s_t',False),('s_q',False),('f_s',False )],0.067)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',True),('f_s',True)],0.052)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',True),('f_s',False)],0.054)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',False),('f_s',True)],0.056)
bn.add('car_s',[('c_c',False),('s_t',True),('s_q',False),('f_s',False)],0.078)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',True),('f_s',True )],0.045)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',True),('f_s',False)],0.031)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',False),('f_s',True )],0.034)
bn.add('car_s',[('c_c',False),('s_t',False),('s_q',False),('f_s',False)],0.023)

# Teste:
print("------------------------------")
print(bn.individual_probabilities())




# -------------------------------------------------------------
# Dominio de pesquisa para testes
# -------------------------------------------------------------


class Cidades(SearchDomain):
    def __init__(self,connections, coordinates):
        self.connections = connections
        self.coordinates = coordinates
    def actions(self,cidade):
        actlist = []
        for (C1,C2,D) in self.connections:
            if (C1==cidade):
                actlist += [(C1,C2)]
            elif (C2==cidade):
               actlist += [(C2,C1)]
        return actlist
    def result(self,cidade,action):
        (C1,C2) = action
        if C1==cidade:
            return C2
    def cost(self,state,action):
        (A,B) = action
        if A != state:
            return None
        for (P,Q,D) in self.connections:
            if (P==A and Q==B) or (P==B and Q==A):
                return D
        return None
    def heuristic(self,state,goal):
        (x1,y1) = self.coordinates[state]
        (x2,y2) = self.coordinates[goal]
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)


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
                      ('Leiria', 'Castelo Branco', 169),
                      ('Figueira', 'Leiria', 62),
                      ('Leiria', 'Santarem', 78),
                      ('Santarem', 'Lisboa', 82),
                      ('Santarem', 'Castelo Branco', 160),
                      ('Castelo Branco', 'Viseu', 174),
                      ('Santarem', 'Evora', 122),
                      ('Lisboa', 'Evora', 132),
                      ('Evora', 'Beja', 105),
                      ('Lisboa', 'Beja', 178),
                      ('Faro', 'Beja', 147),
                      ('Braga', 'Guimaraes', 25),
                      ('Porto', 'Guimaraes', 44),
                      ('Guarda', 'Covilha', 46),
                      ('Viseu', 'Covilha', 57),
                      ('Castelo Branco', 'Covilha', 62)
                     ],

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
                       'Faro': (120, -250),
                       'Guimaraes': ( 71, 300),
                       'Setubal': ( 10, -60),    #new
                       'Covilha': ( 130, 175)
                     } )

# Atalho para obter caminho de c1 para c2 usando strategy:
def search_path(c1,c2,strategy):
    my_prob = SearchProblem(cidades_portugal,c1,c2)
    my_tree = SearchTree(my_prob)
    my_tree.strategy = strategy
    return my_tree.search()


problems = [ SearchProblem(cidades_portugal,'Beja','Viseu'),
             SearchProblem(cidades_portugal,'Braga','Faro'),
             SearchProblem(cidades_portugal,'Coimbra','Evora'),
             SearchProblem(cidades_portugal,'Aveiro','Guarda'),
             SearchProblem(cidades_portugal,'Lisboa','Castelo Branco'),
             SearchProblem(cidades_portugal,'Evora','Figueira'),
             SearchProblem(cidades_portugal,'Guimaraes','Lisboa'),
             SearchProblem(cidades_portugal,'Leiria','Braga'),
             SearchProblem(cidades_portugal,'Faro','Santarem') ]

print("\n------------------------------")
t1 = MyTree(problems[0],'uniform')
print("uniform:",t1.search2())
print(t1.total_nodes,t1.solution_cost)


print("\n------------------------------")
t2 = MyTree(problems[0],'greedy')
print("greedy:",t2.search2())
print(t2.total_nodes,t2.solution_cost)

print("\n------------------------------")
print(profile_strategy('depth',problems))
print("\n------------------------------")
print(profile_strategy('breadth',problems))
print("\n------------------------------")
print(profile_strategy('greedy',problems))


print("\n------------------------------")
t3 = MyTree(problems[0],'uniform')
print("uniform bidirectional:",t3.bidirectional_search())
print(t3.total_nodes,t3.solution_cost)

print("\n------------------------------")
t4 = MyTree(problems[1],'greedy')
print("greedy bidirectional:",t4.bidirectional_search())
print(t4.total_nodes,t4.solution_cost)

print("\n------------------------------")
t5 = MyTree(problems[6],'depth')
print("depth bidirectional:",t5.bidirectional_search())
print(t5.total_nodes,t5.solution_cost)


