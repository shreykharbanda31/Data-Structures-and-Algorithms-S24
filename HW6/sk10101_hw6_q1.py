from DoublyLinkedList import *

class LinkedQueue:

    def __init__(self):
        self.ll = DoublyLinkedList()
        self.curr_node = None

    def __len__(self):
        return len(self.ll)

    def is_empty(self):
        return self.ll.is_empty()

    def enqueue(self,e):
        if self.is_empty():
            self.ll.add_first(e)
            self.curr_node = self.ll.header.next
        else:
            self.ll.add_after(self.curr_node, e)
            self.curr_node = self.curr_node.next

    def dequeue(self):
        if self.is_empty():
            raise Exception("LinkedQueue is empty!")
        else:
            return self.ll.delete_first()
    
    def first(self):
        if self.is_empty():
            raise Exception("LinkedQueue is empty!")
        else:
            return self.ll.header.next.data


