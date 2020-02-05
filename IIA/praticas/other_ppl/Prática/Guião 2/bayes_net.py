from functools import reduce

# Guiao de representacao do conhecimento
# -- Redes de Bayes
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2014
# v1.0 - 2014/11/04
#

# 
class ProbCond:

	def __init__(self,var,mothers,prob):
		self.var = var
		self.mothers = mothers
		self.prob = prob
	def __str__(self):
		return "pc(" + self.var + "," + str(self.mothers) + \
			   "," + str(self.prob) + ")"
	def __repr__(self):
		return str(self)


#   Exemplo:
#      ProbCond("a", [ ("r",True),  ("t",True)  ], 0.95) )
#      Ou seja: a probabilidade condicionada de "alarme" dado que 
#      ocorreu "roubo" e "terramoto" e 95%

# ------------------------------------------------------------

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
			# For all mothers in the dependencies of var being read
			for (mothers,p) in self.dependencies[var].items():
				# If conjunction contains mother, multiply
				if mothers.issubset(conjunction):
					prob*=(p if val else 1-p)
		return prob


	def ind_prob(self, individual):
		var, val = individual
		s=0

		if var not in self.dependencies:
			return None
		
		for (mothers, prob) in self.dependencies[var].items():
			s+=(prob if val else 1-prob)*reduce(lambda r,h: r*self.ind_prob(h), mothers, 1)
		return s
