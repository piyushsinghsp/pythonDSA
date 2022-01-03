def preOrder(root):
	# Your code goes here
    if root==None:
        return 
    print(root.data, end =" ")
    preOrder(root.left)
    preOrder(root.right)
