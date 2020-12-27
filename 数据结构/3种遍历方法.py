class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def insert(self, root, value):
        if root is None:
            return value
        if value.value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root


def pre_order_print(node):
    # self -- left -- right
    print(node.value, end=' ')
    if node.left:
        pre_order_print(node.left)
    if node.right:
        pre_order_print(node.right)


def mid_order_print(node):
    # mid --self -- right
    if node.left:
        mid_order_print(node.left)
    print(node.value, end=' ')
    if node.right:
        mid_order_print(node.right)


def after_order_print(node):
    # left-- right--self
    if node.left:
        after_order_print(node.left)
    if node.right:
        after_order_print(node.right)
    print(node.value, end=' ')


root = Node(5)

tree = BinaryTree()

for i in [2, 11, 7, 3, 9, 8, 4, 6, 1]:
    tree.insert(root, Node(i))
mid_order_print(root)
print(tree)