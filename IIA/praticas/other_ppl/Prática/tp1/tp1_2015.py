from functools import *

viagem=[("avião","SaCarneiro",10,"Stansted",12),
("comboio","Stansted",13,"LiverpoolStreet",14),
("metro","LiverpoolStreet",14,"WestBrompton",15),
("metro","WestBrompton",16,"OxfordStreet",17),
("metro","OxfordStreet",21,"WestBrompton",22),
("metro","WestBrompton",9,"Victoria",10),
("autocarro","Victoria",11,"Bristol",14),
("autocarro","Bristol",10,"Victoria",13),
("metro","Victoria",13,"Westminster",14),
("metro","Westminster",19,"CoventGarden",20),
("metro","CoventGarden",22,"WestBrompton",23),
("metro","WestBrompton",9,"LiverpoolStreet",10),
("metro","LiverpoolStreet",10,"Stansted",11),
("avião","Stansted",12,"SaCarneiro",14)]


# 1
def delete_rep_locals(transp):
	if transp==[]:
		return []

	if len(transp)==1:
		return [transp[0]]

	if transp[0] in transp[1:]:
		return delete_rep_locals(transp[1:])

	return [transp[0]]+delete_rep_locals(transp[1:])

def locais(viagens):
	p = [loc[1] for loc in viagens]
	return delete_rep_locals(p)


#print(locais(viagem))

# 2

def tempo_medio_em_loc(viagens, city):

	tempos = [(time[1],time[2],time[4],time[3]) for time in viagens if time[1]==city or time[3]==city]
	init_list = [time[2] for time in tempos if time[3]==city]
	fin_list = [time[1] for time in tempos if time[0]==city]
	end_t = [t2-t1 for t1,t2 in zip(init_list, fin_list)]
	end_t = list(map(lambda x: x if x>=0 else x+24,end_t))


	return reduce(lambda r,h: h+r, end_t)/len(end_t)

#print(tempo_medio_em_loc(viagem,"WestBrompton"))
#print(tempo_medio_em_loc(viagem,"Victoria"))

# 3
def local_central(viagens):
	loc = locais(viagens)

	lista = list(map(lambda x: reduce(lambda r,h: r+1 if h[1]==x else r,viagens,0),loc))

	r = reduce(lambda r,h: h if h[1]>r[1] else r, zip(loc, lista))

	return r[0]

#print(local_central(viagem))


# 4

def rec_get_length(viagens, central):

	if viagens==[]:
		return [(0,[])]

	r = rec_get_length(viagens[1:],central)

	if viagens[0][3]==central:
		return [(viagens[0][4]-viagens[0][2],[viagens[0][1],viagens[0][3]])]+r


	return [(viagens[0][4]-viagens[0][2]+r[0][0],[viagens[0][1]]+r[0][1])]+r[1:]


def etapas_principais(viagens):

	central = local_central(viagens)

	return rec_get_length(viagens, central)

#list(map(lambda x: print(x), etapas_principais(viagem)))