

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

from Colections import Counter 

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
class Declaration: #permite filtrar as fontes
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
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result

    def show_query_result(self):
        for d in self.query_result:
            print(str(d))
    
    def list_associations(self):
        return list({d.relation.name for d in self.declarations if isinstance(d.relation, Association)}) # passar para set passar para lista
    

    #def list_assosiations(self):
    #    print(self.declarations)
       # return set([d.relation.name for d in self.declarations if isinstance(d.relation, Association)]) # passar para set passar para lista

    def list_entities(self): 
        return list({d.relation.entity1 for d in self.declarations if isinstance(d.relation, Member)})

    def list_existed_users(self):
        return list({d.user for d in self.declarations})
    
    def list_types(self):
        return list(set(
            [d.relation.entity1 for d in self.declarations if isinstance(d.relation, Subtype)] + [d.relation.entity2 for d in self.declarations if isinstance(d.declaration, Subtype) or isinstance(d.relation, Member)]
        ))
    
    def list_entity_associations(self, entity):
        return list({d.relation.name for d in self.declarations if isinstance(d.relation, Association) and (d.relation.entity1 or d.relation.entity2 == entity)})
        #pass

    def list_relations_by_user(self, utilizador):
        return list({d.relation.name for d in self.declarations if d.user == utilizador})
    
    def assocations_by_user(self, utilizador):
        return len({d for d in self.declarations if isinstance(d.relation) and d.user == utilizador})
    
    #def list_local_associations(self, enity):
    #   return list({d.relation.name, d.user...})
    
    def predecessor(self, a, b):
        p = [d.relation.entity2 for d in self.declarations if (isinstance(d.relation, Member) or isistance(d.relation, Subtype)) and ds.relation.entity1 == b] 

        if a in p:
            return True
        
        return any([self.predecessor(a, p1) for p1 in p])

    def predecessor_path(self, a, b):
        p = [d.relation.entity2 for d in self.declarations if (isinstance(d.relation, Member) or isistance(d.relation, Subtype)) and ds.relation.entity1 == b] 
        if a in p: 
            return [a, b]
            
        for path in [self.predecessor_path(a, p1) for p1 in p]:
            if a in path:
                return path + [b]
            return []
    
    def query(self, entity, relation= None):
        pd = [self.query(d.relation.entity2, relation) for d in self.declarations if (isinstance(d.relation, Member) or isistance(d.relation, Subtype)) and ds.relation.entity1 == entity]
        return [item for sublist in pd for item in sublist] + self.query_local(e1 = entity, rel = relation)
        
        
    def query2(self, entity, relation = None):
        pd = [self.query2(d.relation.entity2, relation) for d in self.declarations if (isinstance(d.relation, Member) or isistance(d.relation, Subtype)) and ds.relation.entity1 == entity]
        return [item for sublist in pd for item in sublist if isinstance(item.relation, Association)] + self.query_local(e1 = entity, rel = relation)

    def query_cancel(self, entity, relation = None): # teste, sai
        pd = [self.query_cancel(d.relation.entity2, relation) for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity1 == entity]
        
        local_dec1 = [d for d in self.query_local(e1 = entity, rel = relation) if isinstance(d.relation, Association)]

        return [item for sublist in pd for item in sublist] if item.relation.name not in [d.re.ation.name for d in local_dec1]] + local_dec1]
    
    def query_down(self):
        pd = [self.query_down(d.relation.entity1, relation, False) for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity2 == entity)]

        if skip1st:
            l = []
        else: l = [d for d in self.quey_local( e1 = entity, rel = relation) if isinstance(d.relation, Association)]

        return [item for sublist in pd for item in sublist ] + 1 
    
    def query_induce(self, entity, relation):
        suc = self.query_down(entity, relation)
        c = Counter([d.relation.entity2 for d in suc])
        #c.most_common(1)[0][0]
        for v, count in c.most_common(1):
            return v

    def query_local_assoc(self, entity, relation):
        local = self.query_local(entity, relation)
        if local == []:
            return []

        if isinstance(local[0].relation, AssocNum):

            return sum([l.relation.entity2 for l in local])/len(local)

        elif isinstance(local[0].relation, AssocOne):

            c = Counter([l.relation.entity2 for l in local])
            for v, count in c.most_common(1):
                return v, count/len(local)

        elif isinstance(local[0].relation, Association):
                c = Counter(l.relation.entity2 for l in local])
                l = []
                sumf = 0
                for v, count in c.most_common():
                    l.aooend((v, count/len(local)))
                    sumf += coybt/len(local)
                    if sumf > 0.75:
                        break
                return l
    
    def query_assoc_value(self, entity, assoc):
        
    #
        #if isinstance(e1, Member) == isinstance(e2, Member) or isinstance(e1, Subtype) == isinstance(e2, Subtype): return True
        #return predecessor(e1.)

# Funcao auxiliar para converter para cadeias de caracteres
# listas cujos elementos sejam convertiveis para
# cadeias de caracteres
def my_list2string(list):
   if list == []:
       return "[]"
   s = "[ " + str(list[0])
   for i in range(1,len(list)):
       s += ", " + str(list[i])
   return s + " ]"
    

