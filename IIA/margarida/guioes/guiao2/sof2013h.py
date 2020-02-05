from bayes_net import *

bn = BayesNet()

#add(self,var,mothers,prob)

#variáveis independentes
#US utilizador sobrecarregado
bn.add('US',[],0.60)
#UPT utilizador está a usar o processador de texto
bn.add('UPT',[],0.05)

#variáveis dependentes
#CENL correio eletrónico não lido
bn.add('CENL',[('US',True)],0.90)
bn.add('CENL',[('US',False)],0.001)

#UPA utilizador precisa de ajuda
bn.add('UPA',[('UPT',True)],0.25)
bn.add('UPA',[('UPT',False)],0.004)

#FEUR frequência de utilização do rato
bn.add('FEUR',[('UPA',True),('UPT',True)],0.90)
bn.add('FEUR',[('UPA',False),('UPT',True)],0.90)
bn.add('FEUR',[('UPA',True),('UPT',False)],0.10)
bn.add('FEUR',[('UPA',False),('UPT',False)],0.01)

#UCP utilizador com cara preocupada
bn.add('UCP',[('US',True),('UPA',True)],0.02)
bn.add('UCP',[('US',False),('UPA',True)],0.0011)
bn.add('UCP',[('US',True),('UPA',False)],0.01)
bn.add('UCP',[('US',False),('UPA',False)],0.001)

conj1 = [('US',True),('UPT',True),('CENL',True),('UPA',True),('FEUR',True),('UCP',True)]
print(bn.jointProb(conj1))

conj2 = [('US',False),('UPT',False),('CENL',False),('UPA',False),('FEUR',False),('UCP',False)]
print(bn.jointProb(conj2))
tmp = ['US', 'UPT', 'CENL', 'UPA', 'FEUR', 'UCP']

