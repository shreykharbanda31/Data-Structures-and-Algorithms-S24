from DoublyLinkedList import *

def copy_linked_list(lnk_lst):

    new_lnk_lst = DoublyLinkedList()
    new_lnk_lst.header.next = lnk_lst.header.next
    new_lnk_lst.trailer.prev = lnk_lst.trailer.prev
    return new_lnk_lst

def deep_copy_linked_list(lnk_lst):
    new_lnk_lst = DoublyLinkedList()
    curr_node = lnk_lst.header.next
    while(curr_node is not lnk_lst.trailer):
        if(type(curr_node.data) == int):
            new_lnk_lst.add_last(curr_node.data)
        else:
            new_lnk_lst.add_last(deep_copy_linked_list(curr_node.data))
        curr_node = curr_node.next
    return new_lnk_lst