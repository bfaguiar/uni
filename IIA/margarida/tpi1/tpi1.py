#encoding: utf8
#Ana Margarida Silva 77752
#help from https://docs.python.org/3/library/functions.html#max

from semnet import *
from functools import reduce

class MySemNet(SemanticNetwork):
    def __init__(self):
        SemanticNetwork.__init__(self)

    # local relations of a given entity, including
    # inverse relations
    def query_local_relations(self,e1,relname=None,e2=None):
        if relname==None and e2==None:
            lst = list(set([(d.relation.name, d.relation.entity2) for d in self.declarations    #find all the pairs relation-entity
                    if d.relation.entity1==e1 ]))                                               #linked to the given entity
            lst += list(set([(self.inverse[d.relation.name], d.relation.entity1) for d in self.declarations
                            if d.relation.entity2==e1                                           #then also look for inverse associations
                            and self.inverse.__contains__(d.relation.name)]))
        elif relname == None:                                                                   #find the pairs that link the two given entities
            lst = list(set([(d.relation.name, d.relation.entity2) for d in self.declarations
                    if d.relation.entity1==e1
                    and d.relation.entity2==e2]))
            lst += list(set([(self.inverse[d.relation.name], d.relation.entity1) for d in self.declarations #look for inverse assocs
                            if d.relation.entity2==e1
                            and d.relation.entity1==e2
                            and self.inverse.__contains__(d.relation.name)]))
        else:                                                                                   #finally look for the entities that
            lst = list(set([(d.relation.name, d.relation.entity2) for d in self.declarations    #respond to the given assoc with our
                    if d.relation.entity1==e1                                                   #given entity
                    and d.relation.name==relname]))
            lst += list(set([(self.inverse[d.relation.name], d.relation.entity1) for d in self.declarations
                            if d.relation.entity2==e1
                            and self.inverse.__contains__(d.relation.name)
                            and relname==self.inverse[d.relation.name]]))
        return lst



    # AssocSome associations of a given entity,
    # including inherited; inheritance is cancelled
    # by opposite relations;
    # If needed, you are free to use the optional argument "xpto"
    def query_excluding_opposites(self,entity,assocname,xpto=[]):   #xpto holds opposites
        parents = []
        values = []

        parents = list(set([ d.relation.entity2 for d in self.declarations  #find subtype and member
            if d.relation.entity1==entity                                   #relations for future use
            and not isinstance(d.relation, Association)                     #without repetition
            and not parents.__contains__(d.relation.entity2) ] ))

        for d in self.declarations:
            if d.relation.entity1==entity \
            and not values.__contains__(d.relation.entity2) \
            and not xpto.__contains__(d.relation.entity2):          #find matching relations not in opposite list
                if self.opposite.__contains__(d.relation.name) \
                and self.opposite[d.relation.name]==assocname:      #if an opposite relation is found,
                    xpto += [d.relation.entity2]                    #add it to the opposites list
                elif d.relation.name==assocname:                    #else, the current entity is one
                    values += [d.relation.entity2]                  #of our desired values

        if parents != []:                                           #in case there are other entities i need to
            for elem in parents:                                    #account for, run the query again
                values += self.query_excluding_opposites(elem,assocname, xpto)

        return values

    # a general query method, processing different types of
    # relations according to their specificities
    def query(self,entity,relname):
        lst = []                #contains list
        parents = []            #contains related nodes
        assocFlag = []          #signals the type of association, 0=some, 1=one, 2=num

        parents += list(set([ d.relation.entity2 for d in self.declarations     #already described
                if d.relation.entity1==entity
                and not isinstance(d.relation, Association)
                and not parents.__contains__(d.relation.entity2)] ))

        for d in self.declarations:
            if d.relation.entity1==entity and d.relation.name==relname:
                lst += [d.relation.entity2]                 #adds the entity to the list
                if isinstance(d.relation, AssocSome):       #then signals the association type
                    assocFlag += [0]                        #in case that's the type of relation
                elif isinstance(d.relation, AssocOne):
                    assocFlag += [1]
                elif isinstance(d.relation, AssocNum):
                    assocFlag += [2]

        if assocFlag != []:                                 #in case this iteration found an assoc
            mostCommonAssoc = self.mostFrequent(assocFlag)  #i'll find the most common assoc type
            lst = [lst[i] for i in range(len(lst))          #and remove from the list the values that
                    if assocFlag[i] == mostCommonAssoc]     #aren't from said assoc
            assocFlag = mostCommonAssoc

            if assocFlag == 1:
                lst = [self.mostFrequent(lst)]              #if it's assocOne, choose most frequent
            elif assocFlag == 2:
                lst = [reduce(lambda l1, l2: l1+l2, lst) / len(lst)]    #average value from assocNum

        if parents != []:                                   #in case I have to account for inheritance
            if assocFlag == 0 or assocFlag == []:           #which only happens if it's assocSome or
                for elem in parents:                        #if no result was found locally for the
                    lst += self.query(elem,relname)         #given relname

        return list(set(lst))      #redundancy to fix duplicates on subtype relation

    #auxiliary function to find most frequent element in list
    mostFrequent = lambda s,l : max(l, key=l.count)         #s will receive self, otherwise it won't work


