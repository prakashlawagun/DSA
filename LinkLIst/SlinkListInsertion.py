#Singly LinkedList
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SLinkList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if self.head is None:
            print("Empty Head")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end=" ")
                temp = temp.next

    def insertInBegining(self,newdata):
        newNode = Node(newdata)

        newNode.next = self.head
        self.head = newNode
    def insertInEnding(self,newdata):
        newNode = Node(newdata)
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = newNode
    
    def insertAnyWhere(self,postion,newdata):
        newNode = Node(newdata)
        temp = self.head
        for i in range(1,postion-1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
    
    def removeFromBeginning(self):
        temp = self.head
        self.head = temp.next
        temp.next =None
        del temp
    
    def  removeFromEnd(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next

        prev.next = None
        del temp
    
    def removeFromAnywhere(self,position):
        prev = self.head
        temp = self.head.next

        for i in range(1,position-1):
            temp = temp.next
            prev = prev.next
        
        prev.next = temp.next
        temp.next = None
            

            



n1 = Node(1)
sll = SLinkList()
sll.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
sll.traverse()
print(" ")
sll.insertInBegining(5)
sll.traverse()
print(" ")
sll.insertInEnding(6)
sll.traverse()
print(" ")
sll.insertAnyWhere(6,8)
sll.traverse()
print(" ")
sll.removeFromBeginning()
sll.traverse()
print(" ")
sll.removeFromEnd()
sll.traverse()
print(" ")
sll.removeFromAnywhere(4)
sll.traverse()