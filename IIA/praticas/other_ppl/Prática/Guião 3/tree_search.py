
# Modulo: tree_search
# 
# Fornece um conjunto de classes para suporte a resolucao de 
# problemas por pesquisa em arvore:
#    SearchDomain  - dominios de problemas
#    SearchProblem - problemas concretos a resolver 
#    SearchNode    - nos da arvore de pesquisa
#    SearchTree    - arvore de pesquisa, com metodos para 
#                    a respectiva construcao
#
#  (c) Luis Seabra Lopes, Introducao a Inteligencia Artificial, 2012-2014


# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain:
	# construtor
	def __init__(self):
		abstract
	# lista de accoes possiveis num estado
	def actions(self, state):
		abstract
	# resultado de uma accao num estado, ou seja, o estado seguinte
	def result(self, state, action):
		abstract
	# custo de uma accao num estado
	def cost(self, state, action):
		abstract
	# custo estimado de chegar de um estado a outro
	def heuristic(self, state, goal_state):
		abstract

# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
	def __init__(self, domain, initial, goal):
		self.domain = domain
		self.initial = initial
		self.goal = goal
	def goal_test(self, state):
		return state == self.goal

# Nos de uma arvore de pesquisa
class SearchNode:
	def __init__(self,state,parent,cost=0, prof=0, heur=0): 
		self.state = state
		self.parent = parent
		self.cost = cost
		self.prof = prof
		self.heur = heur
	def __str__(self):
		return "no(" + str(self.state) + "," + str(self.parent) + "," + str(self.cost) +")"
	def __repr__(self):
		return str(self)

	def get_parents(self):
		if(self.parent==None):
			return []
		return [self.parent.state]+self.parent.get_parents()


# Arvores de pesquisa
class SearchTree:

	# construtor
	def __init__(self,problem, strategy='breadth', n=10): 
		self.problem = problem
		root = SearchNode(problem.initial, None, 0, 0)
		self.open_nodes = [root]
		self.strategy = strategy
		self.n = n
		self.term = 1
		self.non_term = 0
		self.ratio = 0
		self.bigger_accum_cost = []
		self.prof = 0
		self.prof_med = 0

	# obter o caminho (sequencia de estados) da raiz ate um no
	def get_path(self,node):
		if node.parent == None:
			return [node.state]
		path = self.get_path(node.parent)
		path += [node.state]
		return(path)

	def update_ratio(self):
		self.ratio = (self.term+self.non_term-1)/self.non_term
		self.prof_med = self.prof/(self.term+self.non_term)

	# procurar a solucao
	def search(self):
		while self.open_nodes != []:
			node = self.open_nodes[0]
			if self.problem.goal_test(node.state):
				self.update_ratio()
				return self.get_path(node), node.cost, node.prof, self.ratio, self.non_term, self.term, self.bigger_accum_cost, self.prof_med

			self.open_nodes[0:1] = []
			
			lnewnodes = []

			for a in self.problem.domain.actions(node.state):
				newstate = self.problem.domain.result(node.state,a)
				
				if newstate not in node.get_parents():
					lnewnodes += [SearchNode(newstate, node, node.cost+self.problem.domain.cost(node.state, (node.state, newstate)), node.prof+1, self.problem.domain.heuristic(node.state, newstate))]
					self.prof += node.prof+1
				
				if len(lnewnodes)!=0:
					self.non_term+=1
					self.term+=len(lnewnodes)-1

			self.add_to_open(lnewnodes)
			self.update_ratio()
		
		return None, 0, 0


	# juntar novos nos a lista de nos abertos de acordo com a estrategia
	def add_to_open(self,lnewnodes):
		if self.strategy == 'breadth':
			self.open_nodes.extend(lnewnodes)
		
		elif self.strategy == 'depth':
			self.open_nodes[0:0] = lnewnodes
		
		elif self.strategy == 'uniform':
			self.open_nodes.extend(lnewnodes)
			self.open_nodes.sort(key=lambda node: node.cost)
		
		elif self.strategy == 'depthwn':
			if(len(lnewnodes)==0 or lnewnodes[0].prof>self.n):
				return
			self.open_nodes[0:0] = lnewnodes

		elif self.strategy == 'greedy':
			self.open_nodes.extend(lnewnodes)
			self.open_nodes.sort(key=lambda node: node.heur)

		elif self.strategy == 'a_star':
			self.open_nodes.extend(lnewnodes)
			self.open_nodes.sort(key=lambda node: node.cost+node.heur)

		for node in lnewnodes:
			if len(self.bigger_accum_cost)>0:
				if self.bigger_accum_cost[0][1]<node.cost:
					self.bigger_accum_cost = [(node.state, node.cost)]
				elif self.bigger_accum_cost[0][1]==node.cost and node.state!=self.bigger_accum_cost[0][0]:
					self.bigger_accum_cost.append((node.state, node.cost))
			else:
				self.bigger_accum_cost.append((node.state, node.cost))
