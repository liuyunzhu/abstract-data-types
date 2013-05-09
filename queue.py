#queue.py

class Queue:
    def __init__(self):
        self._theItems = list()
        
    def isEmpty(self):
        return len(self._theItems) == 0
    
    def length(self):
        return len(self._theItems)

    def display(self):
        print(self._theItems)

    def enqueue(self,item):
        return self._theItems.append(item)

    def dequeue(self):
        return self._theItems.pop(0)
    
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(4)
queue.display()
queue.dequeue()
queue.display()
