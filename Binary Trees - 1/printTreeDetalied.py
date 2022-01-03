def printTreeDetailed(root):
    if root==None:
        return
    print(root.data, end=",")
    if root.left!=None:
        print("L", root.left.data, end=",")
    if root.right!=None:
        print("L", root.right.data, end=",")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)
