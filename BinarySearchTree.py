"""
Node contains :
	-> value
	-> left node
	-> right node
"""
class Node:
	def __init__(self,value=0):
		self.value = value
		self.left = None
		self.right = None

def insert(root,node):
	# no value present
	if root is None:
		root = node
		return root

	# smaller value
	if node.value <= root.value:
		root.left = insert(root.left,node)

	# greater value
	if node.value > root.value:
		root.right = insert(root.right,node)

	return root

def preorderInfo(root,parent=None,str=""):
	if root:
		if parent is None:
			print(root.value,"is root node")
		else:
			print(root.value,str,parent.value)
		preorderInfo(root.left,root,"is leftchild of")
		preorderInfo(root.right,root,"is rightchild of")

def preorder(root):
	if root:
		print(root.value,end=" ")
		preorder(root.left)
		preorder(root.right)

def postorderInfo(root,parent=None,str="is leftchild of"):
	if root:
		postorderInfo(root.left,root,"is leftchild of")
		postorderInfo(root.right,root,"is rightchild of")
		if parent is None:
			print(root.value,"is root node")
		else:
			print(root.value,str,parent.value)

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.value,end=" ")

def inorderInfo(root,parent=None,str=""):
	if root:
		inorderInfo(root.left,root,"is leftchild of")
		if parent is None:
			print(root.value,"is root node")
		else:
			print(root.value,str,parent.value)
		inorderInfo(root.right,root,"is rightchild of")

def inorder(root):
	if root:
		inorder(root.left)
		print(root.value,end=" ")
		inorder(root.right)

def getMinimumValueNode(root):
	if root:
		while root.left is not None:
			root = root.left
		return root
def getMaximumValueNode(root):
	if root:
		while root.right is not None:
			root = root.right
		return root

def deleteNode(root,value):
	if root is None:
		return root

	if value < root.value:
		root.left = deleteNode(root.left,value)

	elif value > root.value:
		root.right = deleteNode(root.right,value)

	else:
		# node has right child
		if root.left is None:
			temp =  root.right
			root = None
			return temp

		# node has left child
		elif root.right is None:
			temp = root.left
			root = None
			return temp
		# node has both left and right child
		else:
			temp = getMinimumValueNode(root.right)
			root.value = temp.value
			root.right = deleteNode(root.right,temp.value)
	return root

def help():
	print("Create object of Node class : \n\t e.g. root = Node(root_value)")
	print("Use methods")
	print("\t'insert' to insert data")
	print("\t\tinsert(root,Node(value))")
	print("\t'preorder' to print preorder traversal")
	print("\t'preorderInfo' to print detailed preorder traversal")
	print("\t'postorder' to print postorder traversal")
	print("\t'postorderInfo' to print detailed postorder traversal")
	print("\t'inorder' to print inorder traversal")
	print("\t'inorderInfo' to print detailed inorder traversal")
	print("\t'getMinimumValueNode' to find node with minimum value")
	

"""
root = Node()
insert(root,Node(10))
insert(root,Node(14))
insert(root,Node(12))
insert(root,Node(13))
insert(root,Node(80))
insert(root,Node(9))
insert(root,Node(17))
insert(root,Node(11))
insert(root,Node(25))
insert(root,Node(24))
insert(root,Node(22))
insert(root,Node(68))


preoder(root)
postorder(root)
inorder(root)
preoder_info(root)
postorder_info(root)
inorder_info(root)

"""