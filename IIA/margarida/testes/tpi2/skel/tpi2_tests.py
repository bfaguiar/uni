#encoding: utf8

from tpi2 import *

z = MySemNet()

z.insert('descartes',Association('socrates','professor','filosofia'))
z.insert('descartes',Subtype('mamifero','vertebrado'))
z.insert('descartes',Subtype('homem','mamifero'))
z.insert('descartes',Association('socrates','professor','matematica'))
z.insert('descartes',Member('platao','homem'))
z.insert('descartes',Association('platao','professor','filosofia'))
z.insert('descartes',Association('socrates','peso',80))
z.insert('descartes',Member('socrates','homem'))
z.insert('descartes',Member('aristoteles','homem'))
z.insert('descartes',Association('mamifero','altura','number','one',1.2))
z.insert('descartes',Association('socrates','altura',1.85))

z.insert('darwin',Subtype('homem','mamifero'))
z.insert('darwin',Subtype('mamifero','vertebrado'))

z.insert('simao',Association('socrates','professor','matematica'))
z.insert('simao',Association('platao','professor','filosofia'))

z.insert('simoes',Association('socrates','professor','matematica'))

z.insert('damasio',Member('socrates','filosofo'))


lobj = z.getObjects()
print("Current objects: {0}\n\n".format(lobj))


for x in lobj:
    print("Types of {0}: {1}".format(x,z.getObjectTypes(x)))
print()

z.insert('tracker',Association('agent','at','cell','one',(0,0),True))

for i in range(10):
    coord = (1,2) if i<7 else (2,3)
    z.insert2('tracker',Association('snake','at',coord))

z.query_local()
z.show_query_result()

