
# Question 1

# Valid Parentheses

'''
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Input: s = "()"
Output: true


Input: s = "()[]{}"
Output: true


Input: s = "(]"
Output: false
'''

# Answer 1

"""from collections import deque

string = input("Enter the string::")

stack = deque(string)

dict = {"(": ")", "{": "}", "[": "]"}

boolStack = []

for itr in range(len(stack)):
    if len(stack) != (0 or 1):    
        if dict.get(stack.popleft()) == stack.popleft():
            boolStack.append(True)
        else:
            boolStack.append(False)
    else:
        print(all(boolStack))
        break"""

# Question 2

# Long Valid Paranthese

'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring.
'''

# Answer 2

"""from collections import deque

string = input("Enter the string::")

stack = deque(string)

dict = {"(": ")", "{": "}", "[": "]"}

sumStack = deque()

for itr in range(len(stack)):
    if len(stack) != (0 or 1):
        if dict.get(stack.popleft()) == stack[0]:
            sumStack.append(2)
        else:
            sumStack.append(0)
    else:
        print(sum(sumStack))
        break"""

# Question 3

'''
Given a string path, which is an absolute path (starting with a slash '/') 
to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory,
a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//')
are treated as a single slash '/'. For this problem, any other format of periods 
such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.

The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
'''

# Answer 3

from collections import deque

string = input("Enter a string::")

stack = deque()

itr = [*string]

for i in itr:
    if '.' != i:
        stack.append(i)
if stack[-1] == '/': stack.pop()
print(*stack)