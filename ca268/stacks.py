class Stack():
    def __init__(self):
        self.lst = []

    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.lst)
    
    def peek(self):
        assert not self.isEmpty()
        return self.lst[-1]
    
    def pop(self):
        #assert not self.isEmpty
        return self.lst.pop()
    
    def push(self, item):
        self.lst.append(item)

stack = Stack()

stack.push('4')
stack.push('3')
stack.push('2')
stack.push('1')
x = stack.pop()
y = stack.pop()
stack.push(y)
stack.push(x)
stack.push('1')
str = ''

print(stack.__len__())
while not stack.isEmpty():
    str += stack.pop()
print(str)
