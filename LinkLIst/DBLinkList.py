#Doubly linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class DLinkList:
    def __init__(self):
        self.head = None
    
    def traverseForward(self):
     if self.head is None:
        print("DB LinkLisk is empty")
     else:
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
    
    def traverseBackward(self):
        print()
        if self.head is None:
            print("DB LinkLisk is empty")
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            while temp is not None:
                print(temp.data,end=" ")
                temp = temp.prev
    
    def insertAtBegining(self,newData):
        print()
        newNode = Node(newData)
        temp = self.head
        temp.prev = newNode
        newNode.next = temp
        self.head = newNode
    
    def insertAtEnding(self,newData):
        print()
        newNode = Node(newData)

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp
    
    def insertAtSpecificPosition(self,newData,postion):
        print()
        newNode = Node(newData)
        temp = self.head

        for i in range(1,postion-1):
            temp = temp.next
        
        newNode.prev = temp
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode
       
    def removeFromBeginning(self):
        print()
        temp = self.head
        self.head = temp.next
        temp.next.prev = None
        del temp
    
    def removeFromEnd(self):
        print()
        before = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            before = before.next
        
        before.next= None
        temp.prev = None
        del temp
    
    def removeFromAnyWhere(self,postion):
        print()
        temp = self.head.next
        before = self.head
        for i in range(1,postion-1):
            temp = temp.next
            before = before.next
        before.next=temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None
        del temp
    
        
        
        
        



        



    
   
n1 = Node(1)
sll = DLinkList()
sll.head = n1
n2 = Node(2)
n2.prev = n1
n1.next = n2
n3 = Node(3)
n3.prev = n2
n2.next = n3
n4 = Node(4)
n4.prev = n3
n3.next = n4
sll.traverseForward()
sll.traverseBackward()
sll.insertAtBegining(5)
sll.traverseForward()
sll.insertAtEnding(6)
sll.traverseForward()
sll.insertAtSpecificPosition(7,4)
sll.traverseForward()
sll.removeFromBeginning()
sll.traverseForward()
sll.removeFromEnd()
sll.traverseForward()
sll.removeFromAnyWhere(3)
sll.traverseForward()




       

    
