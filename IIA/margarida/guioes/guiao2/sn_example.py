



# Redes semanticas
# -- Exemplo
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2016
# 2016/10/12
#


from semantic_network import *

a = Association('socrates','professor','filosofia')
s = Subtype('homem','mamifero')
m = Member('socrates','homem')

da = Declaration('descartes',a)
ds = Declaration('darwin',s)
dm = Declaration('descartes',m)

z = SemanticNetwork()
z.insert(da)
z.insert(ds)
z.insert(dm)
z.insert(Declaration('darwin',Association('mamifero','mamar','sim')))
z.insert(Declaration('darwin',Association('homem','gosta','carne')))

# novas declaracoes

z.insert(Declaration('darwin',Subtype('mamifero','vertebrado')))
z.insert(Declaration('descartes', Member('aristoteles','homem')))

b = Association('socrates','professor','matematica')
z.insert(Declaration('descartes',b))
z.insert(Declaration('simao',b))
z.insert(Declaration('simoes',b))

z.insert(Declaration('descartes', Member('platao','homem')))

e = Association('platao','professor','filosofia')
z.insert(Declaration('descartes',e))
z.insert(Declaration('simao',e))

z.insert(Declaration('descartes',Association('mamifero','altura',1.2)))
z.insert(Declaration('descartes',Association('homem','altura',1.75)))
z.insert(Declaration('simao',Association('homem','altura',1.85)))
z.insert(Declaration('darwin',Association('homem','altura',1.75)))

z.insert(Declaration('descartes', Association('socrates','peso',80)))
z.insert(Declaration('darwin', Association('socrates','peso',75)))
z.insert(Declaration('darwin', Association('platao','peso',75)))


z.insert(Declaration('damasio', Association('filosofo','gosta','filosofia')))
z.insert(Declaration('damasio', Member('socrates','filosofo')))


# Extra - descomentar as restantes declaracoes para o exercicio 3.

#z.insert(Declaration('descartes', AssocNum('socrates','pulsacao',51)))
#z.insert(Declaration('darwin', AssocNum('socrates','pulsacao',61)))
#z.insert(Declaration('darwin', AssocNum('platao','pulsacao',65)))

#z.insert(Declaration('descartes',AssocNum('homem','temperatura',36.8)))
#z.insert(Declaration('simao',AssocNum('homem','temperatura',37.0)))
#z.insert(Declaration('darwin',AssocNum('homem','temperatura',37.1)))
#z.insert(Declaration('descartes',AssocNum('mamifero','temperatura',39.0)))

#z.insert(Declaration('simao',Association('homem','gosta','carne')))
#z.insert(Declaration('darwin',Association('homem','gosta','peixe')))
#z.insert(Declaration('simao',Association('homem','gosta','peixe')))
#z.insert(Declaration('simao',Association('homem','gosta','couves')))

#z.insert(Declaration('damasio', AssocOne('socrates','pai','sofronisco')))
#z.insert(Declaration('darwin', AssocOne('socrates','pai','pericles')))
#z.insert(Declaration('descartes', AssocOne('socrates','pai','sofronisco')))

#print(z.predecessor('vertebrado','socrates'))
#print(z.predecessor_path('vertebrado','socrates'))
#print(z)
#print(z.get_associations())
#print(z.get_infered_objects())
#print(z.get_users())
#print(z.get_types())
#print(z.get_local_associations('homem'))
#print(z.get_user_declarations('darwin'))
#print(z.get_num_user_declarations('darwin'))
#print(z.get_entity_declarations('homem'))
z.query('socrates', 'altura')
z.show_query_result()
