# Pesquisa para resolucao de problemas de atribuicao
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2016
#


class ConstraintSearch:

    # domains é um dicionário com o domínio de cada variável;
    # constaints e' um dicionário com a restrição aplicável a cada aresta;
    def __init__(self,domains,constraints):
        self.domains = domains
        self.constraints = constraints

    def search(self,domains=None):
        
        if domains==None:
            domains = self.domains

        # se alguma variavel tiver lista de valores vazia, falha
        if any([lv==[] for lv in domains.values()]):
            return None

        # se nenhuma variavel tiver mais do que um valor possivel, sucesso
        if all([len(lv)==1 for lv in list(domains.values())]):
            return { v:lv[0] for (v,lv) in domains.items() }
       
        # continuação da pesquisa
        for var in domains.keys():
            if len(domains[var])>1:
                for val in domains[var]:
                    newdomains = dict(domains)
                    newdomains[var] = [val]
                    edges = [(v1,v2) for (v1,v2) in self.constraints if v2==var]
                    newdomains = self.constraint_propagation(newdomains,edges)
                    solution = self.search(newdomains)
                    if solution != None:
                        return solution
                return None

    def constraint_propagation(self,domains,edges):

        while edges!=[]:

            # retirar cabeca da fila de arestas
            (var1,var2) = edges[0]
            edges = edges[1:]

            # remover valores inconsistentes em var1
            constraint = self.constraints[var1,var2]
            domain = []
            for x in domains[var1]:
                possible = False
                for y in domains[var2]:
                    if constraint(var1,x,var2,y):
                        possible = True
                if possible:
                    domain += [x]

            # se removeu, acrescentar arestas que apontam para var1
            if len(domain)<len(domains[var1]):
               domains[var1] = domain
               edges += [(v1,v2) for (v1,v2) in self.constraints if v2==var1]
        return domains 

'''

 # domains é um dicionário com os domínios actuais
    # de cada variável
    # ( ver acetato "Pesquisa com propagacao de restricoes
    #   em problemas de atribuicao - algoritmo" )
    def search(self,domains=None):
        
        if domains==None:
            domains = self.domains

        # se alguma variavel tiver lista de valores vazia, falha
        if any([lv==[] for lv in domains.values()]):
            return None

        # se nenhuma variavel tiver mais do que um valor possivel, sucesso
        if all([len(lv)==1 for lv in list(domains.values())]):
            # se valores violam restricoes, falha
            # ( verificacao desnecessaria se for feita a propagacao
            #   de restricoes )

            for (var1,var2) in self.constraints:
                constraint = self.constraints[var1,var2]
                if not constraint(var1,domains[var1][0],var2,domains[var2][0]):
                    return None 

            return { v:lv[0] for (v,lv) in domains.items() }
       
        # continuação da pesquisa
        # ( falta fazer a propagacao de restricoes )

        for var in domains.keys():
            if len(domains[var])>1:
                for val in domains[var]:
                    newdomains = dict(domains)
                    newdomains[var] = [val]
                    solution = self.search(newdomains)
                    if solution != None:
                        return solution
        

        for var in domains.keys():
            if len(domains[var])>1:
                for val in domains[var]:
                    newdomains = dict(domains)
                    newdomains[var] = [val]
                    for v in [k for k in newdomains.keys() if k != var]:
                        # Pode fazer-se for pelo domínio todo de v.
                        # Ou assumir que as constraints estão todas associadas à mesma variável
                        
                        constraints = self.constraints[var, v] if (var, v) in self.constraints.keys() else self.constraints[v, var] if (v, var) in self.constraints.keys() else None
                        if constraints != None and val in newdomains[v] and (not constraints(var, val, v, val) or not constraints(v, val, var, val)):
                            newdomains[v] = [x for x in domains[v] if x != val]
                        
                        for val2 in domains[v]:
                            constraints = self.constraints[var, v] if (var, v) in self.constraints.keys() else self.constraints[v, var] if (v, var) in self.constraints.keys() else None
                            if constraints != None and (not constraints(var, val, v, val2) or not constraints(v, val, var, val2)):
                                newdomains[v] = [x for x in domains[v] if x != val2]
                    solution = self.search(newdomains)

                    if solution != None:
                        return solution
                return None

'''