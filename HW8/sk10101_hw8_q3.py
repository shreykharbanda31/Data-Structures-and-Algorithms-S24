from BinarySearchTreeMap import *

def restore_bst(prefix_lst):

    def restore_bst_helper(prefix_lst, index, key):

        new_item = BinarySearchTreeMap.Item(prefix_lst[index])
        curr_node = BinarySearchTreeMap.Node(new_item)

        if index == 0:
            return curr_node, curr_node
        connection_node = None

        while prefix_lst[index] < prefix_lst[index - 1]:
            index -= 1
            prev_node = curr_node

            new_item = BinarySearchTreeMap.Item(prefix_lst[index])
            curr_node = BinarySearchTreeMap.Node(new_item)

            if key is not None and curr_node.item.key > key and connection_node is None:
                connection_node = prev_node
            curr_node.left = prev_node
            prev_node.parent = curr_node

            if index == 0:
                if connection_node is None:  
                    return curr_node, curr_node
                return connection_node, curr_node

        prev_connection_node, curr_root = restore_bst_helper(prefix_lst, index - 1, curr_node.item.key)
        prev_connection_node.right = curr_node
        curr_node.parent = prev_connection_node

        if connection_node is None:
            connection_node = curr_node

        if key is not None and key > curr_root.item.key > connection_node.item.key:
            return curr_root, curr_root
        return connection_node, curr_root
        
    bst = BinarySearchTreeMap()
    if len(prefix_lst) == 0:
        return bst
    bst.root = restore_bst_helper(prefix_lst, len(prefix_lst) - 1, None)[1]
    bst.size = len(prefix_lst)
    return bst
    
