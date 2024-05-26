from ArrayDeque import *
from ArrayStack import *

class MidStack:

    def __init__(self):
        self.stack = ArrayStack()
        self.deque = ArrayDeque()
    
    def is_empty(self):
        return self.stack.is_empty() and self.deque.is_empty()

    def __len__(self):
        return len(self.stack)+len(self.deque)
    
    def push(self,e):
        if self.is_empty():
            self.deque.enqueue_last(e)
        elif len(self.stack) < len(self.deque):
            self.stack.push(self.deque.dequeue_first())
            self.deque.enqueue_last(e)
        else:
            self.deque.enqueue_last(e)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.deque.last()
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if not self.deque.is_empty():
            return self.deque.dequeue_last()
        else:
            return self.stack.pop()
    
    def mid_push(self,e):
        if len(self)%2 !=0:
            self.stack.push(self.deque.dequeue_first())
            self.deque.enqueue_first(e)
        else:
            self.deque.enqueue_first(e)

