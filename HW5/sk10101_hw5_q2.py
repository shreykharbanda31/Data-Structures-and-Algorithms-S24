from ArrayStack import *

class MaxStack:

    def __init__(self):
        self.stack = ArrayStack()
        self.maxx = None
    
    def is_empty(self):
        return self.stack.is_empty()
    
    def __len__(self):
        return len(self.stack)
    
    def push(self, e):

        if self.is_empty():
            self.stack.push((e, self.maxx))
            self.maxx = e
        else:
            if self.maxx < e:
                self.stack.push((e, self.maxx))
                self.maxx = e
            else:
                self.stack.push((e,self.maxx))

    def top(self):

        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            temp = self.stack.pop()
            self.maxx = temp[1]
        return temp[0]
        
    def max(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.maxx



    
    
    