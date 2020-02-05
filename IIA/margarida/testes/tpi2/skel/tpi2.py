#encoding: utf8

#from tree_search import *
from semnet import *


class MySemNet(SemanticNetwork):
    def __init__(self,ldecl=[]):
        SemanticNetwork.__init__(self,ldecl)


    # Devolve lista de todos os objectos existentes na rede
    def getObjects(self):
        # IMPLEMENTAR AQUI
        pass

    # Devolve, para o nome de associação dado, uma lista de tuplos 
    # ((t1,t2),freq), em que:
    #   t1 - tipo da primeira entidade da associação
    #   t2 - tipo da segunda entidade da associação
    #   freq - frequência relativa com que ocorre
    def getAssocTypes(self,assocname):
        pass
        # IMPLEMENTAR AQUI


    # Devolve uma lista de tuplos (t,freq) para o objecto dado, 
    # em que:
    #    t - tipo do objecto
    #    freq - frequência com que ocorre
    def getObjectTypes(self,obj):
        pass
        # IMPLEMENTAR AQUI

    def insert2(self,user,rel):
        self.tick += len(rel.name)   # simula a passagem do tempo
        pass
        # IMPLEMENTAR AQUI



