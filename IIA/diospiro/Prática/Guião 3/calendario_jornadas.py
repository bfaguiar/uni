from constraintsearch import *

teams = ["Benfica","Sporting","Porto","Braga","Vitória","Nacional","Marítimo",\
		"Paços de Ferreira","Vitória de Setúbal","Boavista","Rio Ave","Belenenses",\
		"Estoril","Arouca","Moreirense","Tondela","Chaves","Feirense"]

def make_domains(teams):
	games = {"Game "+home_away+str(i):[team for team in teams] for i in range(1,1+(len(teams)//2)) for home_away in ["Casa ","Fora "]}
	return games

# No games between big teams
def games_constraint(g1, t1, g2, t2):

	if t1==t2:
		return False

	if g1==["Benfica"] or g1==["Sporting"] or g1=="Porto":
		if g2==["Benfica"] or g2==["Sporting"] or g2=="Porto":
			return False

	return True

def make_constraints(teams):
	dic = {}
	for i in range(1,1+(len(teams)//2)):
		for h_a1 in ["Casa ","Fora "]:
			for j in range(1,1+(len(teams)//2)):
				for h_a2 in ["Casa ","Fora "]:
					dic[("Game "+h_a1+str(i), "Game "+h_a2+str(j))]=games_constraint

	return dic

cs = ConstraintSearch(make_domains(teams),make_constraints(teams))
print(cs.search())

'''
Domínio:
Equipa 1 Casa: Equipas
Equipa 2 Casa: Equipas
...
Equipa 1 Fora: Equipas
Equipa 2 Fora: Equipas
...

Grafo de Restrições:
Todas as equipas em fora e em casa


'''