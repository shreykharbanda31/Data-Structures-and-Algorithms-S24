from DoublyLinkedList import *

class Integer:
    def __init__(self, num_str):
        self.ll = DoublyLinkedList()
        self.curr_node = self.ll.header
        if len(num_str) != 0:
            for i in range(len(num_str)):
                self.ll.add_after(self.curr_node, int(num_str[i]))
                self.curr_node = self.curr_node.next

    def __add__(self, other):
        final = Integer('')
        if len(self.ll) > len(other.ll):
            larger_stringll = self
            smaller_stringll = other
        elif len(self.ll) == len(other.ll):
            larger_stringll = self
            smaller_stringll = other
        else:
            larger_stringll = other
            smaller_stringll = self

        
        
        if not larger_stringll.ll.is_empty():
            remainder = 0
            for i in range(len(larger_stringll.ll)-len(smaller_stringll.ll)):
                smaller_stringll.ll.add_first(0)
            curr_large_node = larger_stringll.ll.trailer.prev
            curr_small_node = smaller_stringll.ll.trailer.prev
            curr_final_node = final.ll.trailer
            for i in range(len(larger_stringll.ll)-1):
                value = curr_large_node.data + curr_small_node.data
                value2 = (value + remainder) % 10
                final.ll.add_before(curr_final_node,value2)
                remainder = (value + remainder) // 10
                curr_final_node = curr_final_node.prev
                curr_large_node = curr_large_node.prev
                curr_small_node = curr_small_node.prev
     
            value = curr_large_node.data + curr_small_node.data
            value2 = value % 10
            final.ll.add_before(curr_final_node,value + remainder)

        else:
            raise Exception("One of the Integers is empty!")

        return final


    def __repr__(self):
        curr_node = self.ll.header.next
        if len(self.ll) == 1 and curr_node.data == 0:
            return "0"
        while curr_node is not self.ll.trailer:
            if curr_node.data == 0:
                self.ll.delete_first()
                curr_node = self.ll.header.next
            else:
                break

        return "".join(([str(i) for i in self.ll]))

    def __mul__(self, other):
        final = Integer('')
        curr_self_node = self.ll.trailer.prev
        
        for i in range(len(self.ll)):
            curr_other_node = other.ll.trailer.prev
            carry = 0
            temp = Integer("")
            for j in range(len(other.ll)):
                result = curr_self_node.data * curr_other_node.data + carry
                temp.ll.add_first(result % 10)
                carry = result // 10
                curr_other_node = curr_other_node.prev
            if carry != 0:
                temp.ll.add_first(carry)
            for j in range(i):
                temp.ll.add_last(0)
            final = final + temp
            curr_self_node = curr_self_node.prev
        while final.ll.header.next.data == 0 and len(final.ll) > 1:
            final.ll.delete_first()
        return final




