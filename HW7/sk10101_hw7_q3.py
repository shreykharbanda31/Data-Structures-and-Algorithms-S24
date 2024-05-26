from LinkedBinaryTree import *

def is_height_balanced(bin_tree):

    def subtree_is_height_balanced(root):

        if root is None:
            return 0, True
        else:
            left_height, left_balanced = subtree_is_height_balanced(root.left)
            right_height, right_balanced = subtree_is_height_balanced(root.right)
            is_balanced = left_balanced and right_balanced and (abs(left_height-right_height) <=1)
            curr_height = max(left_height, right_height) + 1
            return curr_height, is_balanced

    if bin_tree.root is None:
        raise Exception("Empty Tree not defined")

    height_ans, balanced_ans = subtree_is_height_balanced(bin_tree.root)
    return balanced_ans

