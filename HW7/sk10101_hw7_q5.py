from LinkedBinaryTree import *


def create_expression_tree(prefix_exp_str):

    prefix_exp_lst = prefix_exp_str.split()
    
    def create_expression_tree_helper(prefix_exp_lst, start_pos):
        cursor = prefix_exp_lst[start_pos]
        if cursor not in '+-*/':
            root = LinkedBinaryTree.Node(int(cursor))
            return root, start_pos+1
        left_sub_tree, left_pos = create_expression_tree_helper(prefix_exp_lst, start_pos + 1)
        right_sub_tree, right_pos = create_expression_tree_helper(prefix_exp_lst, left_pos)
        root = LinkedBinaryTree.Node(cursor, left_sub_tree, right_sub_tree)
        return root, right_pos
       


    tree_root, pos = create_expression_tree_helper(prefix_exp_lst, 0)
    
    return LinkedBinaryTree(tree_root)

def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    postfix_exp_str = ''
    for i in tree.postorder():
        postfix_exp_str += str(i.data) + " "
    postfix_exp_str = postfix_exp_str[:-1]
    return postfix_exp_str

print(prefix_to_postfix("* 2 + - 15 6 4"))