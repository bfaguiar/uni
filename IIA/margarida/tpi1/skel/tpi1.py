#encoding: utf8

from semnet import *


class MySemNet(SemanticNetwork):
    def __init__(self):
        SemanticNetwork.__init__(self)

    # local relations of a given entity, including
    # inverse relations
    def query_local_relations(self,e1,relname=None,e2=None):
        pass

    # AssocSome associations of a given entity,
    # including inherited; inheritance is cancelled
    # by opposite relations;
    # If needed, you are free to use the optional argument "xpto"
    def query_excluding_opposites(self,entity,assocname,xpto=[]):
        pass

    # a general query method, processing different types of
    # relations according to their specificities
    def query(self,entity,relname):
        pass

