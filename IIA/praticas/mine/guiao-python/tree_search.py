# este ficheiro é como se fosse uma classe chamada de SearchTree. dentro deste ficheiro/classe tem uma classe chanada de node que tem varias propriedades.

class Node():

    def __init__(self, value = 0, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value
    
    def getNodeValue(self): return self.value
        
    def getLeftChild(self): return self.left

    def getRightChild(self): return self.right

    def setLeftChild(self, node): self.left = node      # entra Node type

    def setRightChild(self, node): self.right = node    # entra Node type
    
    def setNodeValue(self, value): self.value = value   # 
    
    def __str__(self):
        string = "\nnode(value: " + str(self.value)
        if (self.right != None):
            string = string + ", right child: " + str(self.right)
        if (self.left != None):
            string = string + ", left child: " + str(self.left)
        return string + ") \n"


def is_element(root, value):
    if root == None: return False
    if root.getNodeValue() == value: return True
    return is_element(root.getLeftChild(), value) or is_element(root.getRightChild(), value)

def is_isomorfica(root1, root2):
    
    if root1 == None and root2 == None: return True
    if root1 == None or root2 == None: return False
    if root1.getNodeValue() != root2.getNodeValue(): return False
    return is_isomorfica(root1.getRightChild(), root2.getRightChild()) and is_isomorfica(root1.getLeftChild(), root2.getLeftChild())

def is_subtree(tree1, tree2):
    if tree1 == None: return True
    if tree2 == None: return False
    if tree1.getNodeValue() == tree2.getNodeValue() and is_isomorfica(tree1, tree2): return True # se encontrar mos o elemento,  vamos logo verificar os seguintes.
    return is_subtree(tree1, tree2.getLeftChild()) or is_subtree(tree1, tree2.getRightChild()) # se nao, continuar a procurar outro root.

def list_elem(root, f):
    if root == None: return []
    if f(root.getNodeValue()): return [root.getNodeValue()] + list_elem(root.getLeftChild(), f) + list_elem(root.getRightChild(), f)
    return list_elem(root.getLeftChild(), f) + list_elem(root.getRightChild(), f)

def copy_tree(root):
    if root == None: return None
    return Node(root.getNodeValue(), copy_tree(root.getLeftChild()),  copy_tree(root.getRightChild()))

def isSorted(root):

        if root.getNodeValue() == None:
            return True
        if root.getLeftChild() == None and root.getRightChild() == None:
            return True
        if root.getLeftChild() == None:
            if root.getRightChild().getNodeValue() > root.getNodeValue():
                return isSorted(root.getRightChild())            
        if root.getRightChild() == None:
            if root.getLeftChild().getNodeValue() < root.getNodeValue():
                return isSorted(root.getLeftChild())
        if root.getLeftChild().getNodeValue() < root.getNodeValue() and root.getRightChild().getNodeValue() > root.getNodeValue():
            return isSorted(root.getLeftChild()) and isSorted(root.getRightChild())
        return False


def inserir_ordenada(tree, new_value): # mesmo que no
    assert isSorted(tree), "arvore nao ordenada"
    if(tree.getNodeValue() == None): return Node(new_value)
    if new_value == tree.getNodeValue(): return None
    if tree.getNodeValue() > new_value:
        if tree.getLeftChild() == None:
            tree.setLeftChild(Node(new_value))
        return inserir_ordenada(tree.getLeftChild(), new_value)
    if tree.getNodeValue() < new_value:
        if tree.getRightChild() == None:
            tree.setRightChild(Node(new_value))
        return inserir_ordenada(tree.getRightChild(), new_value)


def caminho(no, folha):
    if no == None: return []
    if no.getNodeValue() == folha:
        return [no.getNodeValue()]
    left = caminho(no.getLeftChild(), folha)
    right = caminho(no.getRightChild(), folha)
    if left != []:
        return [no.getNodeValue()] + left
    if right != []:
        return [no.getNodeValue()] + right
    return []
   

no1 = Node(value = 4)
no1.setRightChild(Node(value = 5))
no1.setLeftChild(Node(value = 3))
#no2 = Node(value = 4)
#no2.setRightChild(Node(value = 5))
#no2.setLeftChild(Node(value = 2))
#no2.setLeftChild(Node(value = 10000))
#no1.setLeftChild(Node (value = 10000))

inserir_ordenada(no1, 7)
inserir_ordenada(no1, 5)

print(no1)
inserir_ordenada(no1, 2)
print(caminho(no1, 7))


#print(list_elem(no1, lambda x: x%2 == 0))

#print(isSorted(no1))

#no12 = copy_tree(no1)
#print(no12)

#.getNodeValue().getNodeValue()

#print(is_isomorfica(no1, no2))
#print(is_subtree(no1, no2))
#print(str(e))
#print(str(b))
#print(is_element(b, 3))
#print(is_element(c, 3))
#print(is_element(b, 1))
#print(is_isomorfica(c, b))
#print(is_isomorfica(e, b))
#print(is_isomorfica(tree, tree2))#






