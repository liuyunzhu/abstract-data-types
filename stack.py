#stack.py

class Stack:

    def __init__(self):
        self._theItems = list()

    def isEmpty(self):
        return len(self._theItems) == 0

    def length (self):
        return len(self._theItems)

    def display (self):
        print(self._theItems)
    
    def peek(self):
        if self.isEmpty():
            print ("stack is empty, cannot peek")
        else:
            return self._theItems[-1]

    def pop(self):
        if self.isEmpty():
            print ("stack is empty, cannot pop")
        else:
            return self._theItems.pop()

    def push(self, item):
        self._theItems.append(item)
        

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(5)
stack.display ()
stack.pop()
stack.display()
