#impllementation using deque
'''
from collections import deque

stack = deque()

stack.append("X")
stack.append("Y")
stack.append("Z")
print(stack)

print(stack.pop())
print(stack)

'''

from queue import LifoQueue

stack = LifoQueue(maxsize=3)
stack.put(2)
stack.put(3)
stack.put(4)

print(stack.qsize())
print(stack.queue[-1])
print(stack.queue)
print(stack.get())
print(stack.queue) 
print(stack.full())