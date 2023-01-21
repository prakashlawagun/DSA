class Node:
    def __init__(self,key):
        self.value = key
        self.left = None
        self.right = None
    
    def traverseInPreOrder(self):
        print(self.value)
        if self.left:
            self.left.traverseInPreOrder()
        if self.right:
            self.right.traverseInPreOrder()

    def traverseInPostOrder(self):
        if self.left:
            self.left.traverseInPostOrder()
        if self.right:
            self.right.traverseInPostOrder()
        
        print(self.value)

    def traverseInInOrder(self):
        if self.left:
            self.left.traverseInInOrder()
        print(self.value)

        if self.right:
            self.right.traverseInInOrder()

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.right = Node(3)
print("PreOrder:")
root.traverseInPreOrder()
print("PostOrder:")
root.traverseInPostOrder()
print("InOrder:")
root.traverseInInOrder()
