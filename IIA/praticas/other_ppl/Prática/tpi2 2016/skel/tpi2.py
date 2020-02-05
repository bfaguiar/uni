#encoding: utf8
# Diogo Daniel Soares Ferreira
# Nº 76504

from tree_search import *
from semnet import *
from functools import *

class MySemNet(SemanticNetwork):
	def __init__(self,ldecl=[]):
		SemanticNetwork.__init__(self,ldecl)

	# Retorna todas as associações
	def get_assoc(self, name=None, user=None):
		return [d.relation for d in self.query_local() if d not in self.query_local(rel="member")+self.query_local(rel="subtype") if (name==None or d.relation.name==name) and (user==None or d.user==user)]

	# Retorna a associação entre objetos se objects=1, ou entre tipos
	# se objects=0, com o mesmo nome da associação passada como argumento
	def filter_assoc_types(self, assoc, objects=1):
		return [a for a in self.get_assoc() if a.name==assoc.name and ((objects==1 and a.cardin==None) or (objects==0 and a.cardin!=None))]

	# Devolve lista de todos os objectos existentes na rede
	def getObjects(self):
		all_assoc = self.get_assoc()
		obj_member = [d.relation.entity1 for d in self.query_local(rel="member")]
		assoc_objects = [ filt for assoc in all_assoc for filt in self.filter_assoc_types(assoc, 1)]
		assoc_objects_list = reduce(lambda r,h: r+[h.entity1, h.entity2] if h in assoc_objects else r, all_assoc, [])
		assoc_types = [ filt.default for assoc in all_assoc for filt in self.filter_assoc_types(assoc, 0) if filt.default!=None]
		return list(set(assoc_types+obj_member+assoc_objects_list))

	# Devolve, para o nome de associação dado, uma lista de tuplos 
	# (t1,t2,freq), em que:
	#   t1 - tipo da primeira entidade da associação
	#   t2 - tipo da segunda entidade da associação
	#   freq - frequência relativa com que ocorre
	def getAssocTypes(self,assocname):
		assoc = self.get_assoc(assocname)
		d = {}
		for a in assoc:
			for a2 in self.filter_assoc_types(a, 0):
				if (a2.entity1, a2.entity2) in d:
					d[(a2.entity1, a2.entity2)]+=1
				else:
					d[(a2.entity1, a2.entity2)]=1

		return [ (elem[0], elem[1], d[elem]/sum(d.values())) for elem in d ]


	# Devolve uma lista de tuplos (t,freq) para o objecto dado, 
	# em que:
	#    t - tipo do objecto
	#    freq - frequência com que ocorre
	def getObjectTypes(self,obj):
		all_assoc = self.get_assoc()
		obj_member = [d.relation.entity2 for d in self.query_local(rel="member", e1=obj)]
		
		assoc_cardZero = list(set([ filt for assoc in all_assoc for filt in self.filter_assoc_types(assoc, 0)]))
		obj_assoc_list = list(set([ filt for assoc in all_assoc for filt in self.filter_assoc_types(assoc, 1) if filt.entity1==obj or filt.entity2==obj ]))
		
		default_types = [ (elem.entity2,elem.name) for elem in assoc_cardZero if elem.default==obj]
		herdated_types_1 = [(types.entity1, obj_assoc.name) for types in assoc_cardZero for obj_assoc in obj_assoc_list if obj_assoc.name==types.name and obj_assoc.entity1==obj]
		herdated_types_2 = [(types.entity2, obj_assoc.name) for types in assoc_cardZero for obj_assoc in obj_assoc_list if obj_assoc.name==types.name and obj_assoc.entity2==obj]
		
		herdated = herdated_types_1+herdated_types_2+default_types
		d = {}
		
		for o_type in obj_member:
			if o_type in d:
				d[o_type]+=1
			else:
				d[o_type]=1

		for h_type in herdated:
			if h_type[0] in d:
				d[h_type[0]]+=1/len([elem for elem in herdated if elem[1]==h_type[1]])
			else:
				d[h_type[0]]=1/len([elem for elem in herdated if elem[1]==h_type[1]])

		return [ (elem, d[elem]/sum(d.values())) for elem in d ]


	# Insere uma nova relação "rel" declarada por "user".
	# Se a relação for uma associação fluente entre objectos,
	# tem que fazer a gestão do intervalo de tempo
	# em que a associação se mantém verdadeira
	def insert2(self,user,rel):
		
		if isinstance(rel, Association):
			# Check if parent is fluent
			check_fluent = self.filter_assoc_types(rel, 0)
			fluent = any([assoc_cardZero for assoc_cardZero in check_fluent if assoc_cardZero.fluent])

			if fluent:
				self.tick += len(rel.name)   # simula a passagem do tempo
				existent_assoc = [ elem for elem in self.get_assoc(name=rel.name, user=user) if elem.entity1==rel.entity1]
				if len(existent_assoc)==0:
					rel.time = (self.tick, self.tick)
					self.declarations.append(Declaration(user,rel))
				else:
					valid_assoc = reduce(lambda r,h: h if h.time[1]>r.time[1] else r, existent_assoc)
					if valid_assoc.entity2==rel.entity2:
						valid_assoc.time=(valid_assoc.time[0], self.tick)
					else:
						rel.time = (self.tick, self.tick)
						self.declarations.append(Declaration(user,rel))
				return
		self.insert(user,rel)




class MyTree(SearchTree):

	def __init__(self,problem, strategy='breadth',detect_repeated=False): 
		SearchTree.__init__(self, problem, strategy, detect_repeated)
		self.optimizations = []

	# optimizar e devolver uma solucao previamente 
	# guardada em self.solution
	def optimize(self, res=None):
		if res==None:
			res=self.solution
		if len(res)==1:
			return [res[0]]

		opt = self.optimize(res[1:])

		idx = -1
		for i in range(len(opt[1:])):
			if self.problem.domain.cost(res[0], (res[0], opt[1:][i]))!=None:
				self.optimizations.append((res[0], opt[1:][i]))
				idx = i

		return [res[0]]+opt if idx==-1 else [res[0]]+opt[i:]

