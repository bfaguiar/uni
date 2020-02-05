

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

from collections import Counter

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

class AssocOne(Relation):
    def __init__(self, e1, assoc, e2):
        Relation.__init__(self, e1, assoc, e2)

class AssocNum(Relation):
    def __init__(self, e1, assoc, e2):
        Relation.__init__(self, e1, assoc, e2)

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

    def assoc_names(self):
        return list({ d.relation.name for d in self.declarations if isinstance(d.relation, Association) })
    
    def object_list(self):
        return list({ d.relation.entity1 for d in self.declarations if isinstance(d.relation, Member)})
    
    def users_list(self):
        return list({ d.user for d in self.declarations })
    
    def types_list(self):
        return list(set([d.relation.entity2 for d in self.declarations if isinstance(d.relation, Member) or isinstance(d.relation, Subtype)] + [d.relation.entity1 for d in self.declarations if isinstance(d.relation, Subtype)] ))
    
    def entity_assoclist(self, entity):
        return list({d.relation.name for d in self.declarations if (isinstance (d.relation, Association) and (d.relation.entity1 == entity or d.relation.entity2 == entity))})

    def user_relationlist(self, user):
        return list( { d.relation.name for d in self.declarations if (d.user == user) }) 


    def user_assoclist(self, user):
        return list( { d.relation.name for d in self.declarations if (isinstance(d.relation, Association) and (d.user == user))})
    
    def user_assoccount(self, user):
        return len(self.user_assoclist(user))
    
    def tuple_decl_info(self, entity):
        return list({(d.relation.name, d.user) for d in self.declarations if isinstance(d.relation, Association) and (d.relation.entity1 == entity or d.relation.entity2 == entity)})
    
    def predecessora(self, entityA, entityB):
        lista = [d.relation.entity2 for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and (d.relation.entity1 == entityB)]
        if entityA in lista:
            return True
        else:
            return any([self.predecessora(entityA, e2) for e2 in lista])

    def prodecessora_path(self, A, B):
        lista = [d.relation.entity2 for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and (d.relation.entity1 == B)]
        if A in lista:
            return [A] + [B]
        print([self.prodecessora_path(A, b1) for b1 in lista])
        for path in [self.prodecessora_path(A, b1) for b1 in lista]:
            if A in path:
                return path 
            return []
    
    def query(self, entity, assoc = None):
        entity_tree = [self.query(d.relation.entity2, assoc) for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and (entity == d.relation.entity1)]   
        declarations = [declaration for path in entity_tree for declaration in path]
        return declarations + self.query_local(e1 = entity, rel = assoc)

    def query2(self, entity, relation = None):
        entity_tree = [self.query2(d.relation.entity2, relation) for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and (d.relation.entity1 == entity)]
        return [item for ramo in entity_tree for item in ramo if isinstance(item.relation, Association)] + self.query_local(e1 = entity, rel = relation)
   # def query(self, entity, relation= None):
    #    pd = [self.query(d.relation.entity2, relation) for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity1 == entity]
    #    return [item for sublist in pd for item in sublist] + self.query_local(e1 = entity, rel = relation)
     #   
    def query_cancel(self, entity, assoc = None):
        entity_tree = [self.query_cancel(d.relation.entity2, assoc) for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and (d.relation.entity1 == entity)]
        llocal = [d for d in self.query_local(e1 = entity, rel = assoc) if isinstance(d.relation, Association)] ## vai buscar todas as declaracoes com Association na query local.
        #print("entity:",  entity) #
        #print("entity_tree: ", entity_tree)
        print("llocall: ", llocal)
        ola = [declaration for ramo in entity_tree for declaration in ramo if declaration.relation.name not in [d.relation.name for d in llocal]] + llocal ## retorna as declaracoes 
    #   retorna lista sem, local = posicao atual, entity_tree = posicao a cima.
        #vai retornar a declaracao mais baixa da associacao, neste caso na altura,  
        return ola
    
    def query_down(self, entity, relation, skip1rst = True):
        entity_tree = [self.query_down(d.relation.entity1, relation, False) for d in self.declarations 
                       if (isinstance(d.relation, Member) 
                       or isinstance(d.relation, Subtype)) 
                       and (d.relation.entity2 == entity)]
        print(entity_tree)
        if skip1rst:
            lista = []
        else: lista = [d for d in self.query_local( e1 = entity, rel = relation) if isinstance(d.relation, Association)]
        return [declaration for ramo in entity_tree for declaration in ramo if isinstance(declaration.relation, Association) ] + lista 
           

    def query_induce(self, entity, relation):
        cnt = Counter([declaration.relation.entity2 for declaration in self.query_down(entity, relation)])
        return cnt.most_common(1)[0][0]
    
    def query_local_assoc(self, entity, relation):
        local_declarations = self.query_local(e1 = entity, rel = relation)

        if local_declarations == []:
            return []

        if isinstance(local_declarations[0].relation, Association):
            cnt = Counter([declarations.relation.entity2 for declarations in local_declarations])
            sum_freq = 0
            lista = []
            for entity2, value in cnt.most_common():
                sum_freq = sum_freq + (value/len(local_declarations))
                lista.append((entity2 , value/len(local_declarations)))
                if sum_freq > 0.75:
                    break
            return lista
        
        elif isinstance(local_declarations[0].relation, AssocOne):
            cnt = Counter([declarations.relation.entity2 for declarations in local_declarations])
            return cnt.most_common(1)[0][0], cnt.most_common(1)[0][1]/len(local_declarations)

        elif isinstance(local_declarations[0].relation, AssocNum):
            return sum([d.relation.entity2 for d in local_declarations])/len(local_declarations)
        
    def query_assoc_value(self, E, A, V):
        local_declarations = self.query_local(e1 = E, rel = A)
        check = [d.relation.entity2 == V for d in local_declarations]
        if all(check):
            return V
        
        else:
            cnt = dict((x, y) for x, y in Counter(check).most_common())
            check_predecessor = [d.relation.entity2 == V for d in self.query2(E, A)]
            cnt_predecessor = dict((x, y) for x, y in Counter(check_predecessor).most_common())
            #print(cnt)
            #print(cnt.get("True"))
            return (((cnt.get(True)/len(check))*100) + ((cnt_predecessor.get(True)/len(check_predecessor))*100))/2
    

        #
        #     
    
    #def query_down(self, s_type, association_name):
    #    children = [ d.relation.entity1 for d in self.declarations if (d.relation.entity2==s_type) and (isinstance(d.relation, Subtype) or isinstance(d.relation, Member))]
    #    if children==[]:
    #        return []
    #    dec = [dec for dec in self.declarations for child in children if isinstance(dec.relation, Association) and dec.relation.name==association_name and (dec.relation.entity1==child or dec.relation.entity2==child) ]
    #    dec += [ qu for child in children for qu in self.query_down(child, association_name) ]
    #    
    #    return dec

    #}

# Funcao auxiliar para converter para cadeias de caracteres
# listas cujos elementos sejam convertiveis para
# cadeias de caracteres
def my_list2string(list):
   if list == []:
       return "[]"
   s = "[ " + str(list[0])
   for i in range(1,len(list)):
       s += ";\n" + str(list[i])
   return s + " ]"
    

