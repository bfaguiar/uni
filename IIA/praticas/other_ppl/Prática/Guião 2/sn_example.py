



# Redes semanticas
# -- Exemplo
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2014
# 2014/10/15
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

z.insert(Declaration('descartes', AssocNum('socrates','peso',80)))
z.insert(Declaration('darwin', AssocNum('socrates','peso',75)))
z.insert(Declaration('darwin', AssocNum('platao','peso',75)))

z.insert(Declaration('descartes',AssocNum('homem','altura',1.75)))
z.insert(Declaration('simao',AssocNum('homem','altura',1.85)))
z.insert(Declaration('darwin',AssocNum('homem','altura',1.75)))
z.insert(Declaration('descartes',AssocNum('mamifero','altura',1.2)))

z.insert(Declaration('simao',Association('homem','gosta','carne')))
z.insert(Declaration('darwin',Association('homem','gosta','peixe')))
z.insert(Declaration('simao',Association('homem','gosta','peixe')))
z.insert(Declaration('simao',Association('homem','gosta','couves')))

z.insert(Declaration('damasio', AssocOne('socrates','pai','sofronisco')))
z.insert(Declaration('darwin', AssocOne('socrates','pai','pericles')))
z.insert(Declaration('descartes', AssocOne('socrates','pai','sofronisco')))



#print(z)
#print(z.predecessor('vertebrado','socrates'))
#print(z.predecessor_path('vertebrado','socrates'))
#print(z.assoc_names())
#print(z.get_object_list())
#print(z.get_all_users())
#print(z.get_type())
#print(z.get_assoc_name('mamifero'))
#print(z.get_rel_name('darwin'))
#print(z.get_different_associations('descartes'))
#print(z.get_local_assoc('matematica'))
#print(z.query('socrates','altura'))
#print(z.query2('socrates'))
#print(z.query_cancel('socrates','altura'))
print(z.query_assoc_value("socrates", "altura"))
#print(z.query_down("vertebrado", "altura"))
#print(z.query_induce("vertebrado","altura"))

print(z.query_local_assoc('socrates','pai'))
print(z.query_local_assoc('socrates','peso'))
print(z.query_local_assoc('homem','gosta'))