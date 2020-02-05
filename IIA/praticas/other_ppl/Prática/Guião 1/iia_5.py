class Node():
	def __init__(self, left=None, right=None, value=0):
		self.right = right
		self.left = left
		self.value = value

	def getNodeValue(self):
		return self.value

	def getLeftChild(self):
		return self.left

	def getRightChild(self):
		return self.right

	def setLeftChild(self, node):
		self.left = node

	def setRightChild(self, node):
		self.right = node

	def setNodeValue(self, value):
		self.value = value


	def __str__(self):
		st="\nValor do nó: "+str(self.value)

		if self.left!=None:
			st+="\nFilho Esquerdo: "+str(self.left)
		if self.right!=None:
			st+="\nFilho Direito: "+str(self.right)
		return st


def is_element(root, value):
	if root==None:
		return False

	if root.getNodeValue()==value:
		return True

	return is_element(root.getRightChild(), value) or is_element(root.getLeftChild(), value)

def isomorphic(root1, root2):
	if root1==None and root2==None:
		return True

	elif root1==None or root2==None:
		return False

	elif root1.getNodeValue()!=root2.getNodeValue():
		return False

	else:
		return isomorphic(root1.getLeftChild(), root2.getLeftChild()) and isomorphic(root1.getRightChild(), root2.getRightChild())

def is_subtree(sub, root):
	if sub==None:
		return True

	elif root==None:
		return False

	elif root.getNodeValue()==sub.getNodeValue() and isomorphic(sub, root):
		return True

	return is_subtree(sub, root.getLeftChild()) or is_subtree(sub, root.getRightChild())

def tree_list(root, condition):
	if root==None:
		return []

	elif condition(root.getNodeValue()):
		return [root.getNodeValue()]+tree_list(root.getLeftChild(), condition)+tree_list(root.getRightChild(), condition)

	else:
		return tree_list(root.getLeftChild(), condition)+tree_list(root.getRightChild(), condition)

def copy_tree(root):
	if root==None:
		return None

	left = copy_tree(root.getLeftChild())
	right = copy_tree(root.getRightChild())

	return Node(left=left, right=right, value=root.getNodeValue())

def is_sorted(root):
	if root==None:
		return True
	
	if root.getLeftChild()==None and root.getRightChild()==None:
		return True

	if root.getRightChild()==None:
		if root.getLeftChild().getNodeValue()<=root.getNodeValue():
			return is_sorted(root.getLeftChild())
		else:
			return False

	if root.getLeftChild()==None:
		if root.getRightChild().getNodeValue()>root.getNodeValue():
			return is_sorted(root.getRightChild())
		else:
			return False

	if root.getLeftChild().getNodeValue()<=root.getNodeValue() and root.getRightChild().getNodeValue()>root.getNodeValue():
		return is_sorted(root.getRightChild()) and is_sorted(root.getLeftChild())
	else:
		return False

def insert_tree(root, value):
	if root==None:
		return Node(value=value)

	if value<=root.getNodeValue():
		root.setLeftChild(insert_tree(root.getLeftChild(), value))
	else:
		root.setRightChild(insert_tree(root.getRightChild(), value))
		
	return root


def path_value(root, value):
	if root==None:
		return []

	elif root.getNodeValue()==value:
		return [value]

	left_v=path_value(root.getLeftChild(), value)
	right_v=path_value(root.getRightChild(), value)

	if left_v!=[]:
		return [root.getNodeValue()]+left_v
	if right_v!=[]:
		return [root.getNodeValue()]+right_v

	return []



tree = Node(value=1)
tree.setLeftChild(Node(value=2))
tree.setRightChild(Node(value=3))
tree.getLeftChild().setLeftChild(Node(value=4))

tree2 = Node(value=1)
tree2.setLeftChild(Node(value=2))
tree2.setRightChild(Node(value=3))
tree2.getLeftChild().setLeftChild(Node(value=4))

tree3 = Node(value=3)

tree4 = copy_tree(tree)

tree5 = Node(value=5)
tree5.setLeftChild(Node(value=4))
tree5.setRightChild(Node(value=6))
tree5.getLeftChild().setLeftChild(Node(value=3))
tree5.getLeftChild().getLeftChild().setLeftChild(Node(value=2))

#print(is_element(tree,1))
print(isomorphic(tree, tree2))
#print(is_subtree(tree3, tree))
#print(tree_list(tree, lambda x: x%2==0))
#print(tree4)
#print(is_sorted(tree4))
#print(is_sorted(tree5))
insert_tree(tree,10)
#print(tree)
#print(path_value(tree5,2))


