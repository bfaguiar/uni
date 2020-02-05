class Pai():
	def __init__(self, pai, filho):
		self.pai = pai		
		self.filho = filho

	def __str__(self):
		return str(self.pai)+" é pai de "+str(self.filho)

class Mae():
	def __init__(self, mae, filho):
		self.mae = mae		
		self.filho = filho

	def __str__(self):
		return str(self.mae)+" é mãe de "+str(self.filho)

class Irmao():
	def __init__(self, irmao1, irmao2):
		self.irmao1 = irmao1
		self.irmao2 = irmao2

	def __str__(self):
		return str(self.irmao1)+" é irmão de "+str(self.irmao2)

class Irma():
	def __init__(self, irma1, irma2):
		self.irma1 = irma1		
		self.irma2 = irma2

	def __str__(self):
		return str(self.irma1)+" é irmã de "+str(self.irma2)

class FamilyRelationships():
	def __init__(self, lrel=[]):
		self.lrel = lrel

	def __str__(self):
		c=""
		for rel in self.lrel:
			c+=str(rel)+"\n"

		return c

	def get_parents(self, child):
		mae = None
		pai = None

		for rel in self.lrel:
			if isinstance(rel, Mae) and rel.filho==child:
				mae = rel.mae
			if isinstance(rel, Pai) and rel.filho==child:
				pai = rel.pai

		return (mae,pai)

	def get_childs(self, parent):
		childs = []

		for rel in self.lrel:
			if isinstance(rel, Mae) and rel.mae==parent:
				childs.append(rel.filho)
			if isinstance(rel, Pai) and rel.pai==parent:
				childs.append(rel.filho)

		return childs

	def prog(self, p1, p2):
		par = self.get_parents(p2)
		return p1 in par

	def antecessor(self, ant, ch):
		par = self.get_parents(ch)

		if ant in par or any([self.antecessor(ant, p) for p in par if p!=None]):
			return True

		return False



lrel = [Pai("António","Alberto"), Mae("Antónia", "Alberto"), Pai("António","João"), Pai("João", "Manuel"), Pai("Manuel", "Pedro")]
fam_rel = FamilyRelationships(lrel)
print(fam_rel.get_parents("Alberto"))
print(fam_rel.get_childs("António"))
print(fam_rel.prog("António", "Alberto"))
print(fam_rel.prog("António", "Antónia"))
print(fam_rel.antecessor("António", "Alberto"))
print(fam_rel.antecessor("António", "Pedro"))
print(fam_rel.antecessor("Alberto", "Pedro"))