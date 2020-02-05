
from bayes_net import *


# Exemplo:
# ( ver acetatos das aulas teorico-praticas )
'''
z = BayesNet()
z.add( "r", [], 0.001)
z.add( "t", [], 0.002)
z.add( "a", [ ("r",True),  ("t",True)  ], 0.95)
z.add( "a", [ ("r",True),  ("t",False) ], 0.94)
z.add( "a", [ ("r",False), ("t",True)  ], 0.29)
z.add( "a", [ ("r",False), ("t",False) ], 0.001)
z.add( "j", [ ("a",True) ], 0.9))
z.add( "j", [ ("a",False) ], 0.05))
z.add( "m", [ ("a",True) ], 0.7))
z.add( "m", [ ("a",False) ], 0.1))

print(z.prob_list)

#       p(j & m & a & ~t & ~r)
#       Em Python:
#           jointProb([ ("j",True ), ("m", True ), ("a",True), 
#                          ("t",False), ("r", False)              ] )
#

#print(z.jointProb( [ ("j",True ), ("m", True ), ("a",True), \
#                      ("t",False), ("r", False)              ] ))
#   Exemplo:

print(z.ind_prob("r",True))
print(z.ind_prob("r",False))
print(z.ind_prob("t",True))
print(z.ind_prob("t",False))
print(z.ind_prob("a",True))
print(z.ind_prob("a",False))
print(z.ind_prob("j",True))
print(z.ind_prob("m",True))
'''
# Ex.2
'''
ex2 = BayesNet()
ex2.add("s", [], 0.60)

ex2.add("p", [("s", True), ("a", False)], 0.01)
ex2.add("p", [("s", True), ("a", True)], 0.02)
ex2.add("p", [("s", False), ("a", False)], 0.001)
ex2.add("p", [("s", False), ("a", True)], 0.011)

ex2.add("c", [("s", False)], 0.001)
ex2.add("c", [("s", True)], 0.9)

ex2.add("t", [], 0.05)

ex2.add("a", [("t", True)], 0.25)
ex2.add("a", [("t", False)], 0.004)

ex2.add("r", [("t", False), ("a", True)], 0.1)
ex2.add("r", [("t", False), ("a", False)], 0.01)

ex2.add("r", [("t", True)], 0.9)

print(ex2.ind_prob("a", True))
'''

# Ex. 9

ex2 = BayesNet()
ex2.add("b", [], 0.001)
ex2.add("e", [], 0.02)

ex2.add("a", [("b", True), ("e", True)], 0.9)
ex2.add("a", [("b", True), ("e", False)], 0.9)
ex2.add("a", [("b", False), ("e", True)], 0.1)
ex2.add("a", [("b", False), ("e", False)], 0.001)

ex2.add("m", [("a",True)], 0.95)
ex2.add("m", [("a",False)], 0.001)

ex2.add("j", [("a",True)], 0.9)
ex2.add("j", [("a",False)], 0.0)

print(ex2.jointProb( [ ("m",True), ("a",True)] ))
print(ex2.ind_prob(("b", False)))
print(ex2.ind_prob(("a", True)))
print(ex2.ind_prob(("m", True)))
print(ex2.ind_prob(("j", True)))
