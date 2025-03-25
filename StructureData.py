class Stack:
    def __init__(self):
        #Initialize empty stack
        self.items = []
    
    def push(self, item):
        #Add the item to the top of the stack
        self.items.append(item)
        #Return new length of the stack
        #Ex: push a -> [a] -> len = 1
        #    push b -> [a, b] -> len = 2
        return len(self.items)
    
    def pop(self):
        #Return none if the stack is empty
        if self.isEmpty():
            return None
        #Remove & return the item at the top of the stack
        return self.items.pop()
    
    #Check if the stack is empty
    def isEmpty(self):
        return len(self.items) == 0
    
    #Return/Fetch the item at the top of the stack
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def length(self):
        return len(self.items)

#Validating string function
def isValid(s):
    #Create new stack everytime function is called
    stack = Stack()
    #Dictionary to match brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    #Iteration
    for char in s:
        #if char is an opening bracket, push to stack
        if char in mapping.values():
            stack.push(char)
        #if char is a closing bracket, check 
        # 1. stack empty = false
        # 2. compare last item in stack with closing bracket
        elif char in mapping.keys():
            if stack.isEmpty() or stack.pop() != mapping[char]:
                return False
        else:
            return False
    
    return stack.isEmpty()

# Test
print(isValid("()"))  # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))  # Output: False
print(isValid("([])"))  # Output: True
