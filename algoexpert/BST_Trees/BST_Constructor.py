# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
					
		

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		if value<self.value: 
			if self.left == None: # no left child node, create it
				self.left = BST(value)
				return
			else: # send it further down
				insert_recursion(self.left,value)
			
		if value>=self.value: 
			if self.right == None: # no right child node, create it
				self.right = BST(value)
				return
			else: # send it further down
				insert_recursion(self.right,value)				
		
        return self

    def contains(self, value):		
		if self.value == None:
			return False
		
		if self.value == value: # node contains the value
			print("found first")
			print(self.value,value)
			return True
		
		if value < self.value:
			ret = traverse_cotains_recursion_DFS(self.left,value)
		if value > self.value:
			ret =  traverse_cotains_recursion_DFS(self.right,value)
			
			print(ret)
		return ret
		
		
		
		
    def remove(self, value):
		

	#if node doesnt contain the value we want
		if self.value != value:
			if value<= self.value:
				self.left = delete_recursion(self.left,value)

			
			if value > self.value:
				self.right = delete_recursion(self.right,value)

	
		#If node contains the value we want to delete
		if self.value == value:
		
		
			#no children
			if (self.left == None) and (self.right == None):

				return self #single node we do nothing
			# one children, we link the branch left to the parent of the delete node
			if self.left == None:


				self.value = self.right.value
				self.left = self.right.left
				self.right = self.right.right
				
				return self
			
			
			
			if self.right ==None:
				temp = self.left
				self.value = temp.value
				self.left = temp.left
				self.right = temp.right
				
				return self
			# two children look link
			# Find inorder successor(min value on the right) of the node. Copy contents of the inorder successor to the node and delete the inorder successor
			# Find min value of right sub tree

			min_value = find_min_recursion(self.right)
			print(min_value)
			self.value = min_value #node takes the min value of the right tree and we delete the node that contains that min value from the right
			self.right = delete_recursion(self.right,min_value)

        return self


	
	
	
	
	
	
	
	
	
	
def traverse_cotains_recursion_DFS(tree,value):
	# edge case
	if tree == None:
		return False
		
	if tree.value == value: # node contains the value
		print("recursion found")
		print(tree.value,value)
		return True
		
	# search for the value in the children if the node doesnt have it
	
	if value < tree.value:
		left = traverse_cotains_recursion_DFS(tree.left,value)	
		return left
	if value > tree.value:
		right = traverse_cotains_recursion_DFS(tree.right,value)
		return right
	
			
#################	
	
def insert_recursion(tree,value):
	
	if value<tree.value: 
		if tree.left == None: # no left child node, create it
			tree.left = BST(value)
			return
		else: # send it further down
			insert_recursion(tree.left,value)
			
	if value>=tree.value: 
		if tree.right == None: # no right child node, create it
			tree.right = BST(value)
			return
		else: # send it further down
			insert_recursion(tree.right,value)

			
##########			
			
def find_min_recursion(tree):
	#smaller values will bne constantly on the left
	if tree.left == None: #nothing else on the left
		return tree.value
	
	return find_min_recursion(tree.left) #look further down and return the min value found bellow
	
			
def delete_recursion(tree,value):
#https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
	if tree ==None:
		return None
	
	#if node doesnt contain the value we want
	if tree.value != value:
		if value<= tree.value:
			tree.left = delete_recursion(tree.left,value)
			return tree
			
		if value > tree.value:
			tree.right = delete_recursion(tree.right,value)
			return	tree
	
	#If node contains the value we want to delete
	if tree.value == value:
		
		#no children
		if tree.left == None and tree.right == None:
			return None #we return None essentially deleting the node
		# one children, we link the branch left to the parent of the delete node
		if tree.left == None:
			return tree.right 
		if tree.right ==None:
			return tree.left 
		# two children look link
		# Find inorder successor(min value on the right) of the node. Copy contents of the inorder successor to the node and delete the inorder successor
		# Find min value of right sub tree
		min_value = find_min_recursion(tree.right)
		tree.value = min_value #node takes the min value of the right tree and we delete the node that contains that min value from the right
		tree.right = delete_recursion(tree.right,min_value)
		return tree
		
		
		
		
		