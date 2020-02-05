#encoding: utf8

from tree_search import *
from semnet import *

#HIDE
from collections import Counter
#SHOW

class MySemNet(SemanticNetwork):
    def __init__(self,ldecl=[]):
        SemanticNetwork.__init__(self,ldecl)


    # Devolve lista de todos os objectos existentes na rede
    def getObjects(self):
        # IMPLEMENTAR AQUI
        pass
#HIDE
        lobj = set()
        for d in self.declarations:
           if isinstance(d.relation,Member):
               lobj.add(d.relation.entity1)
#              print("{0} {1}".format("Member",d.relation.entity1))
           if isinstance(d.relation,Association) and d.relation.cardin==None:
               lobj.update([d.relation.entity1,d.relation.entity2])
#              print("{0} {1} {2}".format("Association",d.relation.name,[d.relation.entity1,d.relation.entity2]))
        return list(lobj)
#SHOW

    # Devolve, para o nome de associação dado, uma lista de tuplos 
    # ((t1,t2),freq), em que:
    #   t1 - tipo da primeira entidade da associação
    #   t2 - tipo da segunda entidade da associação
    #   freq - frequência relativa com que ocorre
    def getAssocTypes(self,assocname):
        pass
        # IMPLEMENTAR AQUI
#HIDE
        lassoctypes = []
        for d in self.declarations:
           if isinstance(d.relation,Association) and \
                   d.relation.cardin!=None and d.relation.name == assocname:
               lassoctypes = [(d.relation.entity1,d.relation.entity2)]
        return itemFreqs(lassoctypes)
#SHOW


    # Devolve uma lista de tuplos (t,freq) para o objecto dado, 
    # em que:
    #    t - tipo do objecto
    #    freq - frequência com que ocorre
    def getObjectTypes(self,obj):
        pass
        # IMPLEMENTAR AQUI
#HIDE
        lobjtypes = []
        for d in self.declarations:
           if d.relation.name=='member' and d.relation.entity1==obj:
               lobjtypes += [(d.relation.entity2,1.0)]
           if isinstance(d.relation,Association) and d.relation.cardin==None \
                   and obj in [d.relation.entity1,d.relation.entity2]:
               lassoctypes = self.getAssocTypes(d.relation.name)
               if obj==d.relation.entity1:
                  lobjtypes += [(t1,f) for ((t1,t2),f) in lassoctypes]
               else:
                  lobjtypes += [(t2,f) for ((t1,t2),f) in lassoctypes]
        d = {}
        for (t,f) in lobjtypes:
            d[t] = d.setdefault(t,0) + f
        total = 0.0
        for (t,f) in d.items():
            total += f
        s = sorted(d.items(),key=lambda i : i[1])
        return [(t,f/total) for (t,f) in s]
#SHOW

    # Insere uma nova relação "rel" declarada por "user".
    # Se a relação for uma associação fluente entre objectos,
    # tem que fazer a gestão do intervalo de tempo
    # em que a associação se mantém verdadeira
    def insert2(self,user,rel):
        self.tick += len(rel.name)   # simula a passagem do tempo
        pass
        # IMPLEMENTAR AQUI
#HIDE
        if isinstance(rel,Association) and rel.cardin==None:
            lassocs = [ d.relation for d in self.declarations 
                if d.relation.name==rel.name and d.relation.cardin=='one' ]
#           print(lassocs)
            r = Association(rel.entity1,rel.name,rel.entity2)
            if lassocs!=[] and lassocs[0].fluent:
                l1 = []
                l2 = []
                for d in self.declarations:
                    if d.user==user and d.relation.getTriple()==rel.getTriple():
                        l1 += [d]
                    else:
                        l2 += [d]
#               print("l1={0} l2={1}".format(l1,l2))
                self.declarations = l2
                if l1==[]:
                   r.time = (self.tick,self.tick)
                else:
                    old = l1[0]
                    extend = True
                    for d in self.declarations:
                        if d.user==user and d.relation.entity1==rel.entity1 \
                                and d.relation.name==rel.name \
                                and d.relation.entity2!=rel.entity2 \
                                and d.relation.time[0]>=old.relation.time[1]: 
                            extend = False
                            break
                    if extend:
                        r.time = (old.relation.time[0],self.tick)
                    else:
                        self.declarations.append(old)
        else:
            r = rel
        self.declarations.append(Declaration(user,r))
#SHOW


#HIDE
def itemFreqs(lst):
    c = Counter(lst)
    total = 0.0
    for (t,n) in c.items():
        total += n
    s = sorted(c.items(),key=lambda i : i[1])
    return [(t,n/total) for (t,n) in s]
#SHOW


class MyTree(SearchTree):

    # optimizar e devolver uma solucao previamente 
    # guardada em self.solution
    def optimize(self):
        pass
        # IMPLEMENTAR AQUI
#HIDE
        path = self.solution
        if path == None:
            return None
        optimized_path = path[:]
        optimized = False
        self.optimizations = []
        changed = True
        while changed and len(optimized_path)>2:
            changed = False
            for i in range(len(optimized_path)-2):
                for j in range(i+2,len(optimized_path)):
                    a = optimized_path[i]
                    b = optimized_path[j]
                    la = self.problem.domain.actions(a)
                    if (a,b) in la:
                        optimized_path[i:j+1] = [a,b]
                        self.optimizations += [(a,b)]
                        changed = True
                        break
                if changed:
                    break
        return optimized_path
#SHOW


