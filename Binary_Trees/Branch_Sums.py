# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	ret = []
	cusum = 0
	
	def recurs(root,cusum):
		
		if (root.left == None) and (root.right==None):
			ret.append(cusum+root.value)
			
		#left
		if root.left != None:
			recurs(root.left,cusum + root.value)
			
		if root.right != None:
			recurs(root.right,cusum + root.value)
			
	recurs(root,cusum)
	return ret