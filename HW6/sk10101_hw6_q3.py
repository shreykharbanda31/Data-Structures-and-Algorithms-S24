from DoublyLinkedList import *

class CompactString:
    def __init__(self, orig_str):
        self.ll = DoublyLinkedList()
        self.curr_node = self.ll.header
        if len(orig_str) != 0:
            ct = 1
            for i in range(1,len(orig_str)):
                if orig_str[i-1] == orig_str[i]:
                    ct += 1
                else:
                    self.ll.add_after(self.curr_node, (orig_str[i-1],ct))
                    self.curr_node = self.curr_node.next
                    ct = 1
            self.ll.add_after(self.curr_node, (orig_str[-1],ct))
        

    def __add__(self, other):
        final = CompactString('')
        final_curr_node = final.ll.header
        curr_node = self.ll.header.next
        for i in range(len(self.ll)):
            final.ll.add_after(final_curr_node, curr_node.data)
            final_curr_node = final_curr_node.next
            curr_node = curr_node.next
        curr_node = other.ll.header.next
        for j in range(len(other.ll)):
            final.ll.add_after(final_curr_node, curr_node.data)
            final_curr_node = final_curr_node.next
            curr_node = curr_node.next
        return final

    def __lt__(self, other):

        curr_self_node = self.ll.header.next
        curr_other_node = other.ll.header.next
        i=1
        j=1
        while curr_self_node is not self.ll.trailer and curr_other_node is not other.ll.trailer:
            if ord(curr_self_node.data[0]) != ord(curr_other_node.data[0]):
                if ord(curr_self_node.data[0]) >= ord(curr_other_node.data[0]):
                    return False
                return True
            i+=1
            j+=1
            if i == curr_self_node.data[1]+1:
                curr_self_node = curr_self_node.next
                i=1
            if j == curr_other_node.data[1]+1:
                curr_other_node = curr_other_node.next
                j=1
        return True
            
            
    def __le__(self, other):

        is_equal = True
        curr_self_node = self.ll.header.next
        curr_other_node = other.ll.header.next
        i=1
        j=1
        while is_equal and curr_self_node is not self.ll.trailer and curr_other_node is not other.ll.trailer:
            if ord(curr_self_node.data[0]) != ord(curr_other_node.data[0]):
                is_equal = False
            i+=1
            j+=1
            if i == curr_self_node.data[1]+1:
                curr_self_node = curr_self_node.next
                i=1
            if j == curr_other_node.data[1]+1:
                curr_other_node = curr_other_node.next
                j=1
        return is_equal or self < other
        

    def __gt__(self, other):
        return not self <= other
        
    def __ge__(self, other):
        return not self < other

    def __repr__(self):
        final = ''
        curr_node = self.ll.header.next
        for i in range(len(self.ll)):
            for j in range(curr_node.data[1]):
                final += curr_node.data[0]
            curr_node = curr_node.next
        return final


