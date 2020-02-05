

class BayesNet:

    def __init__(self,ldep={}):
        self.dependencies = ldep

    # Os dados estao num dicionario (var,dependencies)
    # em que as dependencias de cada variavel
    # estao num dicionario (mothers,prob);
    # "mothers" e' um frozenset de pares (mothervar,boolvalue)
    def add(self,var,mothers,prob):
        self.dependencies.setdefault(var,{})[frozenset(mothers)] = prob

    # Probabilidade conjunta de uma dada conjuncao 
    # de valores das variaveis da rede
    def jointProb(self,conjunction):
        prob = 1.0
        for (var,val) in conjunction:
            for (mothers,p) in self.dependencies[var].items():
                if mothers.issubset(conjunction):
                    prob*=(p if val else 1-p)
        return prob


    def singleProb(self,var,val):
        prob = 0
        lvars = self.ancestors(var)
        lcomb = [ c+[(var,val)] for c in self.varCombin(lvars) ]

        for conj in lcomb:
            prob += self.jointProb(conj)
        return prob

    def varCombin(self, lvars):
        if lvars == []:
            return [[]]
        rec = self.varCombin(lvars[1:])
        v = lvars[0]
        return [ c+[(v,True)] for c in rec ] + [ c+[(v,False)] for c in rec ]

    def ancestors(self, var):
        lvars = [ v for (v,x) in list(self.dependencies[var].keys())[0] ]
        lvars2 = lvars

        for v in lvars:
            lvars2 += self.ancestors(v)

        return list(set(lvars2))


