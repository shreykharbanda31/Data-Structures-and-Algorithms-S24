from ArrayStack import *

class Queue:

    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()

    def __len__(self):
        return len(self.stack1)

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()
    
    def enqueue(self, e):
            self.stack1.push(e)

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
        

    
