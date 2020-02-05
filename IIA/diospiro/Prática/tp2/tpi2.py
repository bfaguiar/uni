from semantic_network import *
from tree_search import *
from functools import *

class MySN(SemanticNetwork):
	def query_dependents(self, e):
		childs = [ dec.relation.entity1 for dec in self.query_local(e2=e, rel="subtype")+self.query_local(e2=e, rel="member") ]
		local_dependents = [ dec.relation.entity1 for dec in self.query_local(e2=e, rel="depends")]
		t = [l for l in local_dependents+childs if self.query_local(e2=l, rel="subtype")==[]]
		t1 = [d for dep in local_dependents for d in self.query_dependents(dep)]
		t2 = [d for dep in childs for d in self.query_dependents(dep)]
		return set(t+t1+t2)

	def query_causes(self, e):
		ancestors = [ dec.relation.entity2 for dec in self.query_local(e1=e, rel="subtype")+self.query_local(e1=e, rel="member") ]
		local_dependents = [ dec.relation.entity2 for dec in self.query_local(e1=e, rel="depends") if self.query_local(e2=dec.relation.entity2, rel="subtype")==[]]
		herd_dep = [cause for ent in ancestors for cause in self.query_causes(ent)]
		return set(herd_dep+local_dependents+[cause for ent in local_dependents for cause in self.query_causes(ent)])

	def query_causes_sorted(self, e):
		causes = self.query_causes(e)
		causes_time = [ (cause, self.time(cause)) for cause in causes ]
		return sorted(causes_time, key=lambda c: c[1])

	def time(self, cause):
		dt = [ qu.relation.entity2 for qu in self.query_local(e1=cause) if qu not in self.query_local(e1=cause, rel="subtype") and qu not in self.query_local(e1=cause, rel="member") and qu.relation.name=="debug_time"]
		return reduce(lambda r,h: r+h, dt, 0)/len(dt)

class MyTree(SearchTree):
	def __init__(self, problem, strategy, extra=None):
		SearchTree.__init__(self, problem, strategy, extra)
		self.optimizations = []
		self.solution_cost = None
		self.solution_length = None
		self.tree_size = 1

	def optimize(self, res=None):
		if res==None:
			res=self.result
		if len(res)==1:
			return [res[0]]

		opt = self.optimize(res[1:])

		idx = -1
		for i in range(len(opt[1:])):
			if self.problem.domain.cost(res[0], (res[0], opt[1:][i]))!=None:
				self.optimizations.append((res[0], opt[1:][i]))
				idx = i

		
		if idx==-1:
			return [res[0]]+opt
		else:
			return [res[0]]+opt[i:]

	# procurar a solucao
	def search2(self):
		self.open_nodes[0].arg3=0
		self.open_nodes[0].arg4=self.problem.domain.heuristic(self.open_nodes[0].state, self.problem.goal)
		self.open_nodes[0].arg5=0
		while self.open_nodes != []:
			node = self.open_nodes[0]
			if self.problem.goal_test(node.state):
				self.result = self.get_path(node)
				self.solution_cost = node.arg3
				print(node.arg3)
				self.solution_length = node.arg5
				return self.result
			self.open_nodes[0:1] = []
			actions = self.problem.domain.actions(node.state)
			lnewnodes = []
			for a in actions:
				newstate = self.problem.domain.result(node.state,a)
				if newstate not in self.get_path(node) and self.problem.domain.cost(newstate, (newstate,node.state))+node.arg3<=self.extra:
					newnode = SearchNode(newstate,node,node.arg3+self.problem.domain.cost(newstate, (newstate,node.state)), self.problem.domain.heuristic(newstate, self.problem.goal), node.arg5+1)
					lnewnodes += [newnode]
			self.add_to_open(lnewnodes)
		return None

	def astar_add_to_open(self,lnewnodes):
		self.open_nodes.extend(lnewnodes)
		self.tree_size+=len(lnewnodes)
		self.open_nodes.sort(key=lambda node: node.arg3+node.arg4)