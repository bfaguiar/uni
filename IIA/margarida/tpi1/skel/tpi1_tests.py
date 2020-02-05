#encoding: utf8

from tpi1 import *


z = MySemNet()

z.insert('descartes',Subtype('mammal','vertebrate'))
z.insert('darwin',Subtype('mammal','vertebrate'))
z.insert('darwin',AssocSome('mammal','likes','milk'))

z.insert('descartes',Subtype('man','mammal'))
z.insert('darwin',Subtype('man','mammal'))
z.insert('darwin',AssocSome('man','likes','meat'))
z.insert('bacon',AssocOne('man','likes','vegetables'))
z.insert('descartes',AssocNum('man','hasWeight',80))
z.insert('descartes',AssocNum('man','hasWeight',70))
z.insert('descartes',AssocNum('man','hasHeight',1.75))
z.insert('descartes',AssocNum('man','hasHeight',1.80))

z.insert('bacon',AssocSome('philosopher','likes','philosophy'))

z.insert('descartes',Member('socrates','man'))
z.insert('damasio',Member('socrates','philosopher'))
z.insert('descartes',AssocSome('socrates','professorOf','philosophy'))
z.insert('descartes',AssocSome('socrates','professorOf','mathematics'))
z.insert('simoes',AssocNum('socrates','professorOf','mathematics'))
z.insert('simao',AssocSome('socrates','professorOf','mathematics'))
z.insert('descartes',AssocNum('socrates','hasHeight',1.75))
z.insert('nunes',AssocOne('socrates','hasHeight',1.70))
z.insert('bacon',AssocNum('socrates','hasHeight',1.80))
z.insert('simao',AssocOne('socrates','hasFather','sophroniscus'))
z.insert('nunes',AssocOne('socrates','hasFather','sophroniscus'))
z.insert('aristotle',AssocOne('socrates','hasFather','plato'))
z.insert('bacon',AssocNum('socrates','hasFather','plato'))
z.insert('simao',AssocOne('socrates','hasMother','phaenarete'))
z.insert('socrates',AssocSome('socrates','likes','sophroniscus'))
z.insert('sophroniscus',AssocSome('socrates','likes','phaenarete'))
z.insert('bacon',AssocSome('socrates','likes','mathematics'))
z.insert('bacon',AssocSome('socrates','dislikes','meat'))


z.insert('descartes',Member('plato','man'))
z.insert('descartes',AssocSome('plato','professorOf','philosophy'))
z.insert('simao',AssocSome('plato','professorOf','philosophy'))
z.insert('simao',AssocSome('aristotle','hasFather','ariston'))

z.insert('descartes',Member('aristotle','man'))
z.insert('simao',AssocOne('aristotle','hasFather','nicomachus'))

z.addInverse('hasFather','fatherOf')
z.addOpposite('likes','dislikes')



