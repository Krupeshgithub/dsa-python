# collections.deque

from collections import deque

stack = deque("stack")

stack.append("R") # add a new entry to the right side
stack.appendleft("L") # add a new entry to the left side

stack.pop() # retrun and remove the rightmost item
stack.popleft() # return and remove the leftmost item

stack[0] # peek at leftmost item
stack[-1] # peek at rightmost item

'R' in stack # search the deque

stack.extend("Extend") # multiple elements at once

stack.rotate(1) # right rotation (move one steps left to right)
stack.rotate(-1) # left rotation (move one steps right to left)

stack.clear() # empth the deque
stack.pop() # cannot pop from an empty deque (error: IndexError)
