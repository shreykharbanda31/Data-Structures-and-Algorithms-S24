from BinarySearchTreeMap import *

def find_min_abs_difference(bst):

    def find_min_abs_difference_helper(curr_node):

        if curr_node.left is None and curr_node.right is None:
            return (curr_node.item.key, curr_node.item.key, None)
        else:
            if curr_node.left is None and curr_node.right is not None:
                right_tuple = find_min_abs_difference_helper(curr_node.right)
                minimum = curr_node.item.key
                maximum = right_tuple[1]
                min_difference = (right_tuple[0] - curr_node.item.key, right_tuple[2])

            elif curr_node.left is not None and curr_node.right is None:
                left_tuple = find_min_abs_difference_helper(curr_node.left)
                minimum = left_tuple[0]
                maximum = curr_node.item.key
                min_difference = (curr_node.item.key - left_tuple[1], left_tuple[2])

            else:
                left_tuple = find_min_abs_difference_helper(curr_node.left)
                right_tuple = find_min_abs_difference_helper(curr_node.right)
                minimum = left_tuple[0]
                maximum = right_tuple[1]
                min_difference = (curr_node.item.key - left_tuple[1], right_tuple[0] - curr_node.item.key, left_tuple[2], right_tuple[2])
            return (minimum, maximum, min(i for i in min_difference if i is not None))

    if bst.root is None:
        raise Exception("Not defined on an Empty Tree")

    if bst.root.left is None and bst.root.right is None:
        raise Exception("Not defined on a Tree with a single node")
    return find_min_abs_difference_helper(bst.root)[2]