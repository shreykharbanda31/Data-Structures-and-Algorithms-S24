from LinkedBinaryTree import *

def min_and_max(bin_tree):

    def subtree_min_and_max(root):
        if root.left is None and root.right is None:
            return (root.data, root.data)
        elif root.left is not None and root.right is None:
            return (min(subtree_min_and_max(root.left)[0],root.data),max(subtree_min_and_max(root.left)[1],root.data))
        elif root.right is not None and root.left is None:
            return (min(root.data,subtree_min_and_max(root.right)[0]),max(root.data,subtree_min_and_max(root.right)[1]))
        else:
            return (min(subtree_min_and_max(root.left)[0], root.data,subtree_min_and_max(root.right)[0]),max(subtree_min_and_max(root.left)[1],root.data,subtree_min_and_max(root.right)[1]))

    if len(bin_tree) == 0:
        raise Exception("Cannot find max/min for an empty tree")
    return subtree_min_and_max(bin_tree.root)


a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)
bin_tree = LinkedBinaryTree(f)
print(min_and_max(bin_tree))