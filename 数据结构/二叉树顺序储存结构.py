"""

二叉树的顺序储存结构代码实现

"""
from binarytree import Node


class TreeNode():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree():
    def insert(self, root, value):
        if root is None:
            return value
        elif value.value < root.value:
            root.left = self.insert(root.left, value)
        elif value.value > root.value:
            root.right = self.insert(root.right, value)

root_1 = Node(5)
tree = BinaryTree()
for i in [1,2,3,4,5,6,7,8,9]:
    tree.insert(root_1, Node(i))
print(tree)