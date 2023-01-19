'''
class CircleQueue:
    def __init__(self,k):
        self.k = k
        self.queue= [None]*k
        self.head=self.tail= -1

    def enqueue(self,item):
        if ((self.tail+1)%self.k == self.head):
            print("Queue is full")
        
        elif(self.head ==-1):
            self.tail=0
            self.head=0
            self.queue[self.tail]=item
        else:
            self.tail = (self.tail+1)%self.k
            self.queue[self.tail]=item
    
    def dequeue(self):
        if(self.head==-1):
            print("Queue is empty")
        
        elif(self.head==self.tail):
            temp= self.queue[self.head]
            self.head= -1
            self.tail= -1
            return temp
        else:
            temp=self.queue[self.head]
            self.head = ((self.head+1)%self.k)
            return temp

    def display(self):
        if(self.head ==-1):
            print("Empty  queue")
        
        elif(self.head<=self.tail):
            for i in range(self.head,self.tail+1):
                print(self.queue[i])
                print()
        
        else:
            for i in range(self.head,self.k):
                print(self.queue[i])
            for i in range(0,self.tail+1):
                print(self.queue[i])

obj = CircleQueue(5)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)

obj.display()

print()
obj.dequeue()
obj.display()
'''
class MyCircleQueue:
    def __init__(self,k):
        self.k = k
        self.queue = [None]*k
        self.rear=self.front=-1

    def enqueue(self,item):
        if(self.front==-1 and self.rear == -1):
            self.front = self.rear = 0
            self.queue[self.rear] = item
        elif((self.rear+1)%self.k==self.front):
            print("Queue is full")
        
        else:
            self.rear=(self.rear+1)%self.k
            self.queue[self.rear]=item
    
    def dequeue(self):
        if(self.front==-1 and self.rear):
            print("Queue is empty")
        
        elif(self.front== self.rear):
            self.rear = self.front = -1
        
        else:
            print("Queue:",self.queue[self.front])
            self.front = (self.front+1)%self.k



    def display(self):
        i = self.front
        if(self.front == -1 and self.rear == -1):
            print("Queue is empty")
        
        else:
            while(i != self.rear):
                print(self.queue[i])
                i = (i+1)%self.k
            print(self.queue[i])

             



obj = MyCircleQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.display()
obj.dequeue()
obj.display()
obj.enqueue(6)
obj.display()




