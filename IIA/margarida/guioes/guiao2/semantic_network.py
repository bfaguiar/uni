

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

    #1
    def predecessor(self, pred,desc):
        lst = [ d.relation.entity1 for d in self.declarations
                  if d.relation.entity2 == pred
                  if not isinstance(d.relation,Association) ]

        for x in lst:
            if x == desc:
                return True
            if self.predecessor(x,desc):
                return True
        return False


    #2
    def predecessor_path(self, pred,desc):
        lst = [ d.relation.entity1 for d in self.declarations
                  if d.relation.entity2 == pred
                  if not isinstance(d.relation,Association) ]

        for x in lst:
            if x == desc:
                return [pred,x]
            if self.predecessor_path(x,desc):
                return [pred] + self.predecessor_path(x,desc)
        return []

    #3
    def get_associations(self):
        return list(set([ d.relation.name for d in self.declarations
                if isinstance(d.relation,Association) ] ) )

    #4
    def get_infered_objects(self):
        return list(set([ d.relation.entity1 for d in self.declarations
                if isinstance(d.relation,Member)]))

    #5
    def get_users(self):
        return list(set([ d.user for d in self.declarations]))

    #6
    def get_types(self):
        return list(set([ d.relation.entity2 for d in self.declarations
                          if isinstance(d.relation,Member)]))

    #7
    def get_local_associations(self, entity):
        return list(set([ d.relation.name for d in self.declarations
                          if isinstance(d.relation,Association) and (d.relation.entity1 == entity)]))

    #8
    def get_user_declarations(self, u):
        return list(set([ d.relation.name for d in self.declarations
                        if isinstance(d.relation,Association) and (d.user == u)]))

    #9
    def get_num_user_declarations(self, u):
        tmp = list(set([ d.relation.name for d in self.declarations
                        if isinstance(d.relation,Association) and (d.user == u)]))
        return len(tmp)

    #10
    def get_entity_declarations(self, entity):
        tmp = []
        for d in self.declarations:
            if isinstance(d.relation,Association) and d.relation.entity1 == entity:
                tmp += [(d.relation.name,d.user)]
        return tmp

    #11a
    def query(self, entity, assoc=None):
        lst = [ d.relation.entity2 for d in self.declarations
                  if d.relation.entity1 == entity
                  if not isinstance(d.relation,Association) ]


        ldecl = [ d for d in self.declarations
                  if isinstance(d.relation, Association)
                  and d.relation.entity1==entity
                  and (d.relation.name == assoc or assoc == None) ]

        for x in lst:
            ldecl += self.query(x,assoc)

        self.query_result = ldecl
        return self.query_result

    #11b
    def query2(self, entity, assoc=None):
        lst = [ d.relation.entity2 for d in self.declarations
                  if d.relation.entity1 == entity
                  if not isinstance(d.relation,Association) ]


        ldecl = self.query(entity, assoc)

        for x in lst:
            ldecl +=  [ d for d in self.declarations
                  if isinstance(d.relation, Association)
                  and d.relation.entity1==entity
                  and (d.relation.name == assoc or assoc == None) ]

        self.query_result = ldecl
        return self.query_result


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
    


