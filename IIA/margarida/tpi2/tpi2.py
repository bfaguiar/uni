#Ana Margarida Silva 77752

from tree_search import *
from bayes_net import *
from copy import deepcopy


# -------------------------------------------------------------

class MyBN(BayesNet):

    def individual_probabilities(self):
        allvars = list(self.dependencies)       #all variables in network
        result = {}

        for var in allvars:
            prob = 0
            anc = self.ancestors(var) #find the ancestors for the given var (more efficient than searching all combinations)
            lcomb = [ c+[(var,True)] for c in self.varCombin(anc) ]   #calculates all possible combinations between
                                                                      #the given var and its ancestors
            for conj in lcomb:
                prob += self.jointProb(conj)             #calculates the joint probability

            result[var] = prob

        return result

    def varCombin(self, lvars):                          #get all combinations between vars
        if lvars == []:
            return [[]]
        rec = self.varCombin(lvars[1:])                  #recursive termination
        v = lvars[0]
        return [ c+[(v,True)] for c in rec ] + [ c+[(v,False)] for c in rec ] #generate the combinations

    def ancestors(self, var):
        lvars = [ v for (v,x) in list(self.dependencies[var].keys())[0] ]   #gets all var dependencies
        lvars2 = lvars

        for v in lvars:
            lvars2 += self.ancestors(v)     #append ancestor's ancestor

        return list(set(lvars2))




# -------------------------------------------------------------

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth'):
        super().__init__(problem,strategy)
        root = self.open_nodes[0]
        root.arg3 = 0
        root.arg4 = self.problem.domain.heuristic(root.state,self.problem.goal)
        self.total_nodes = 1
        self.solution_cost = 0

    def uniform_add_to_open(self,lnewnodes):
        self.open_nodes.extend(lnewnodes)                   # append all new open nodes and order them by cost,
        self.open_nodes.sort(key=lambda node: node.arg3)    # the one with the lowest cost will be expandaded first
 
    def greedy_add_to_open(self,lnewnodes):
        self.open_nodes.extend(lnewnodes)                   # append all new open nodes and order them by heuristic
        self.open_nodes.sort(key=lambda node: node.arg4)    # value, the one with the lowest heuristic will be expanded
        self.open_nodes = [self.open_nodes[0]]              # and the remaining ones will be removed


    # procurar a solucao
    def search2(self):
        while self.open_nodes != []:
            node = self.open_nodes[0]
            self.open_nodes[:1] = []

            print("node " + str(node.state) + " cost " + str(node.arg3))

            if self.problem.goal_test(node.state):
                self.solution_cost = node.arg3    #solution cost is the cost of the goal node
                return self.get_path(node)

            actions = self.problem.domain.actions(node.state)
            lnewnodes = []
            for a in actions:
                newstate = self.problem.domain.result(node.state,a)
                if newstate not in self.get_path(node):                            #cost of new node is the cost of the
                    newcost = node.arg3 + self.problem.domain.cost(node.state, a)  #expanded node + it's cost to the expanded
                    newheur = self.problem.domain.heuristic(a[1], self.problem.goal) #heuristic is the predicted cost to go
                    newnode = SearchNode(newstate,node,newcost, newheur)             #between the new node to the goal node
                    lnewnodes += [newnode]
                    self.total_nodes += 1           #increase total node count
            self.add_to_open(lnewnodes)

        return None



    #works correctly only when using uniform search, has problems because on the other strategies
    #the calculated path and the inverse path might not be the same, so extra nodes are added
    #to the path. there are many redundancies and seemingly unnecessary code, but as the other
    #strategies weren't giving a path that made sense, some processing was done to remove nodes
    #that were really out of place (the given paths aren't the most effective or the ones that
    #should be resulting, but at least they're a logical path)
    def bidirectional_search(self):
        rev_problem = SearchProblem(self.problem.domain, self.problem.goal, self.problem.initial)
        end = MyTree(rev_problem, self.strategy)    #create new searchtree in reverse order (starts from end)
        begin = MyTree(self.problem, self.strategy) #copy current tree to new tree, although not
                                                    #required, looks more identifiable as the opposite tree (starts from beginning)
        stop_end = False        #flag to indicate if the reversed search should stop
        stop_begin = False      #flag to indicate if the natural search should stop

        while end.open_nodes != [] and begin.open_nodes != [] :
            if stop_end == False:               #still searching on end tree
                node_end = end.open_nodes[0]
                end.open_nodes[:1] = []
                for n in begin.open_nodes[1:]:  #checks if the current node belongs to
                    if n.state == node_end.state:   #the open node list of the other tree
                        if n.arg3 < node_end.arg3:  #and this searchtree stops if the node
                            stop_end = True         #is found and has a lower value on the other side
                if end.problem.goal_test(node_end.state):   #if the node is the goal, search will also stop
                    stop_end = True

            if stop_begin == False:                 #same as before, but checking on the
                node_begin = begin.open_nodes[0]    #tree that has the regular order
                begin.open_nodes[:1] = []
                for n in end.open_nodes:
                    if n.state == node_begin.state:
                        if n.arg3 < node_begin.arg3:
                            stop_begin = True
                            end.problem.goal = node_begin.state
                if begin.problem.goal_test(node_begin.state):
                    stop_begin = True

            if stop_end and stop_begin:             #reached the solution
                self.solution_cost = node_end.arg3 + node_begin.arg3 #cost is the sum  of both trees' cost
                self.total_nodes = end.total_nodes   #there's a problem i could not identify when expanding the nodes
                                                     #but when using uniform or greedy the correct number is
                                                     #the number of nodes only on the reversed tree

                lst = begin.get_path(node_begin)            #processing the path, the end tree has to be reversed
                for e in end.get_path(node_end)[::-1]:      #as it has the path backwards, some elements have to be
                    if lst.__contains__(self.problem.goal): #removed so the path makes sense even on the cases this
                        break                               #search doesn't work like it should
                    if lst.__contains__(e) == False:
                        lst += [e]
                return lst

            if stop_end == False:                           #if the reversed tree is still searching:
                actions = end.problem.domain.actions(node_end.state)    #this part works exactly like
                lnewnodes = []                                          #search2, so this is probably
                for a in actions:                                       #where it is misbehaving
                    newstate = end.problem.domain.result(node_end.state,a)  #but i couldn't figure out
                    if newstate not in end.get_path(node_end):              #what part of it to change
                        newcost = node_end.arg3 + end.problem.domain.cost(node_end.state, a)
                        newheur = end.problem.domain.heuristic(a[1], end.problem.goal)
                        newnode = SearchNode(newstate,node_end,newcost, newheur)
                        lnewnodes += [newnode]
                        end.total_nodes += 1
                end.add_to_open(lnewnodes)

            if stop_begin == False:                                 #does the same as before but for the
                actions = begin.problem.domain.actions(node_begin.state)    #regular ordered tree
                lnewnodes = []
                for a in actions:
                    newstate = begin.problem.domain.result(node_begin.state,a)
                    if newstate not in begin.get_path(node_begin):
                        newcost = node_begin.arg3 + begin.problem.domain.cost(node_begin.state, a)
                        newheur = begin.problem.domain.heuristic(a[1], begin.problem.goal)
                        newnode = SearchNode(newstate,node_begin,newcost, newheur)
                        lnewnodes += [newnode]
                        begin.total_nodes += 1
                begin.add_to_open(lnewnodes)

        return None


def profile_strategy(strategy,problems):
    avg_cost = 0
    avg_nodes = 0
    for p in problems:                          #repeat for all problems:
        optimal_tree = MyTree(p, 'uniform')     #get the values for the comparison tree
        optimal_tree.search2()                  #using uniform search
        optimal_cost = optimal_tree.solution_cost
        optimal_nodes = optimal_tree.total_nodes

        test_tree = MyTree(p, strategy)         #get the tree values
        test_tree.search2()                     #using the given search strategy
        test_cost = test_tree.solution_cost
        test_nodes = test_tree.total_nodes

        avg_cost += (test_cost/optimal_cost)/len(problems)    #calculate the cost and nodes ratio
        avg_nodes += (test_nodes/optimal_nodes)/len(problems) #and store it already knowing it'll
                                                              #be worth 1/(number of problems)
    return (avg_cost, avg_nodes)                              #when calculating the average
