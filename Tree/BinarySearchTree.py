class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
       

#Inorder traversal function
def inOrder(root):
    if root is not None:
        inOrder(root.left)

        print(str(root.key)+"->",end=" ")

        inOrder(root.right)

#Insert node to tree
def insertNode(node,key):
    #return a new node if tree is empty or null
    if node is None:
        return Node(key)
    
    #Traverse and insert the node in the right place
    if key < node.key:
        node.left = insertNode(node.left,key)
    else:
        node.right = insertNode(node.right,key)
    
    return node

#Find inorder successor is defined
def minValue(node):
    current = node
    #find the left most leaf is node
    while(current.left is not None):
        current = current.left
    
    return current

#Deleting a node is done
def deleteNode(root,key):
    #return back if tree is empty
    if root is None:
        return root
    # find the node  to be deleted from the tree
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif(key > root.key):
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            del root
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        #if the node has 2 children
        #placed the inorder successor in position of the node to be deleted
        temp = minValue(root.right)

        root.key = temp.key

        root.right = deleteNode(root.right,temp.key)
    return root

        
root = None
root = insertNode(root,9)
root = insertNode(root,4)
root = insertNode(root,2)
root = insertNode(root,7)
root = insertNode(root,8)
root = insertNode(root,11)
root = insertNode(root,15)
root = insertNode(root,5)

print("Inorder traversal:",end=" ")
inOrder(root)

print("\nDelete 11:")
root = deleteNode(root,11)
print("In order traversal")
inOrder(root)





        