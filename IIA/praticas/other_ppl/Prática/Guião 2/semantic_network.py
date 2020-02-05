

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2015
# v1.7 - 2015/10/13
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

from functools import reduce

class Relation:
	def __init__(self,e1,rel,e2):
		self.entity1 = e1
#       self.relation = rel  # obsoleto
		self.name = rel
		self.entity2 = e2
	def __str__(self):
		return self.name + "(" + str(self.entity1) + "," + \
			   str(self.entity2) + ")"
	def __repr__(self):
		return str(self)


# Subclasse Association
class Association(Relation):
	def __init__(self,e1,assoc,e2):
		Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
	def __init__(self,sub,super):
		Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
	def __init__(self,obj,type):
		Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
	def __init__(self,user,rel):
		self.user = user
		self.relation = rel
	def __str__(self):
		return "decl("+str(self.user)+","+str(self.relation)+")"
	def __repr__(self):
		return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

class AssocOne(Relation):
	def __init__(self, e1, rel, e2):
		Relation.__init__(self, e1, rel, e2)


class AssocNum(Relation):
	def __init__(self, e1, rel, e2):
		Relation.__init__(self, e1, rel, e2)


# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:

	def __init__(self,ldecl=[]):
		self.declarations = ldecl

	def __str__(self):
		return my_list2string(self.declarations)

	def insert(self,decl):
		self.declarations.append(decl)

	def query_local(self,user=None,e1=None,rel=None,e2=None):
		self.query_result = \
			[ d for d in self.declarations
				if  (user == None or d.user==user)
				and (e1 == None or d.relation.entity1 == e1)
				#and (rel == None or d.relation.name == rel)
				and (rel == None or isinstance(d.relation, rel))
				and (e2 == None or d.relation.entity2 == e2) ]
		return self.query_result

	def show_query_result(self):
		for d in self.query_result:
			print(str(d))

	def predecessor(self, e1, e2):
		ancestors = [d.relation.entity2 for d in self.query_local(e1=e2, rel=Subtype) + self.query_local(e1=e2, rel=Member)]

		if e1 in ancestors:
			return True
		else:
			return any([self.predecessor(e1, a) for a in ancestors])

	def predecessor_path(self, e1, e2):
		ancestors = [d.relation.entity2 for d in self.query_local(e1=e2, rel=Subtype) + self.query_local(e1=e2, rel=Member)]
		
		if e1 in ancestors:
			return [e1, e2]

		else:
			path_ancestors = [ p for p in [self.predecessor_path(e1,a) for a in ancestors] if p != None]
			
			if path_ancestors != []:
				return path_ancestors[0] + [e2]
			else:
				return None


	def assoc_names(self):
		associations = [d for d in self.query_local(rel=Association)]
		return list(set([d.relation.name for d in associations]))

	def get_object_list(self):
		return list(set([d.relation.entity1 for d in self.query_local(rel=Member)]))

	def get_all_users(self):
	   return list(set([dec.user for dec in self.query_local()]))

	def get_type(self):
		sub1 = [dec.relation.entity1 for dec in self.query_local(rel=Subtype)]
		sub2 = [dec.relation.entity2 for dec in self.query_local(rel=Subtype)]
		memb = [dec.relation.entity2 for dec in self.query_local(rel=Member)]
		return list(set(sub1+sub2+memb))

	def get_assoc_name(self, ent):
		return list(set([d.relation.name for d in self.query_local(e1=ent, rel=Association) + self.query_local(e2=ent, rel=Association)]))
		
	def get_rel_name(self, user):
		return list(set([d.relation.name for d in self.query_local(user=user)]))

	def get_different_associations(self, user):
		return len(set([d.relation.name for d in self.query_local(user=user, rel=Association)]))

	def get_local_assoc(self, entity):
		e1 = [(d.relation.name, d.user) for d in self.query_local(e1=entity, rel=Association)]
		e2 = [(d.relation.name, d.user) for d in self.query_local(e2=entity, rel=Association)]
		return e1+e2

	def query(self, entity, association_name=None):
		local_associations = [ d for d in self.declarations if (d.relation.entity1==entity or d.relation.entity2==entity) and isinstance(d.relation, Association) and (association_name==None or association_name==d.relation.name)]

		ancestors = [ d.relation.entity2 for d in self.declarations if (d.relation.entity1==entity) and (isinstance(d.relation, Subtype) or isinstance(d.relation, Member))]

		if ancestors==[]:
			self.query_result = local_associations
		else:
			self.query_result = [query for a in ancestors for query in self.query(a, association_name) if self.query(a, association_name)!=[] ]+local_associations

		return self.query_result

	def query2(self, entity, relation_name=None):
		local_relations = [ d for d in self.declarations if (d.relation.entity1==entity or d.relation.entity2==entity) and (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and (relation_name==None or relation_name==d.relation.name)]

		self.query_result = self.query(entity, relation_name) + local_relations

		return self.query_result

	def query_cancel(self, entity, association_name=None, herd=[]):
		local_associations = [ d for d in self.declarations if (d.relation.entity1==entity or d.relation.entity2==entity) and isinstance(d.relation, Association) and (association_name==None or association_name==d.relation.name) and d.relation.name not in herd ]
		herd = herd+[ local_a.relation.name for local_a in local_associations ]

		ancestors = [ d.relation.entity2 for d in self.declarations if (d.relation.entity1==entity) and (isinstance(d.relation, Subtype) or isinstance(d.relation, Member))]

		if ancestors==[]:
			self.query_result = local_associations
		else:
			self.query_result = [query for a in ancestors for query in self.query_cancel(a, association_name, herd) if self.query_cancel(a, association_name, herd)!=[] ]+local_associations

		return self.query_result

	def query_assoc_value(self, e, a):
		local_associations = [ d.relation.entity2 for d in self.declarations if d.relation.entity1==e and isinstance(d.relation, Association) and d.relation.name==a ]
		
		if len(set(local_associations))==1:
			return query_local_assoc[0]

		herdated_assoc = [ d.relation.entity2 for d in self.query(entity=e, association_name=a) if (d.relation.entity2 not in local_associations)]

		f = dict()
		for v in set(local_associations + herdated_assoc):
			f[v] = (self.percentagem(v, local_associations) + self.percentagem(v, herdated_assoc))/2

		return max(f, key=f.get) if len(f)>0 else {}

	def percentagem(self, value, lista):
		return lista.count(value)/len(lista) if len(lista)>0 else 0


	def query_down(self, s_type, association_name):
		children = [ d.relation.entity1 for d in self.declarations if (d.relation.entity2==s_type) and (isinstance(d.relation, Subtype) or isinstance(d.relation, Member))]

		if children==[]:
			return []

		dec = [dec for dec in self.declarations for child in children if isinstance(dec.relation, Association) and dec.relation.name==association_name and (dec.relation.entity1==child or dec.relation.entity2==child) ]

		dec += [ qu for child in children for qu in self.query_down(child, association_name) ]

		return dec

	def query_induce(self, s_type, association_name):
		down = self.query_down(s_type, association_name)
		
		res = [ d.relation.entity1 if d.relation.entity2==association_name else d.relation.entity2 for d in down  ]
		dic = {}
		
		for r in res:
			if r in dic:
				dic[r]+=1
			else:
				dic[r]=0


		return max(dic, key=dic.get)

	def query_local_assoc(self, e, association_name):
		total=0
		n=0
		dic = {}
		dic2 = {}

		for d in self.declarations:
			if d.relation.name==association_name and d.relation.entity1==e:
				if isinstance(d.relation, AssocNum):
					total+=d.relation.entity2
					n+=1

				elif isinstance(d.relation, AssocOne):
					if d.relation.entity2 in dic:
						dic[d.relation.entity2]+=1
					else:
						dic[d.relation.entity2]=1
				elif isinstance(d.relation, Association):
					if d.relation.entity2 in dic2:
						dic2[d.relation.entity2]+=1
					else:
						dic2[d.relation.entity2]=1

		if dic:
			return (max(dic, key=dic.get), dic[max(dic, key=dic.get)]/sum(dic.values()))
		elif n!=0:
			return total/n
		elif dic2:
			dic2_sorted = [(k, dic2[k]) for k in sorted(dic2, key=dic2.get, reverse=True)]

			length = reduce(lambda r,h: r+h[1], dic2_sorted, 0)
			for d in dic2_sorted:
				dic[d[0]]=d[1]/length
				if(sum(dic.values())>=0.75):
					return [ (d,dic[d]) for d in dic ]
			return [ (d,dic[d]) for d in dic ]
		else:
			return None



# Funcao auxiliar para converter para cadeias de caracteres
# listas cujos elementos sejam convertiveis para
# cadeias de caracteres
def my_list2string(list):
   if list == []:
	   return "[]"
   s = "[ " + str(list[0])
   for i in range(1,len(list)):
	   s += ", \n" + str(list[i])
   return s + " ]"
	

