"""

python二叉树实现

"""
class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self):
        self.root = None
    def make_tree(self, treeNode):
        self.root = treeNode
    def insert(self, treeNode):
        tList = []
        def insert_node(treenode, p , treeNode):
            if treenode.left is None:
                treenode.left = treeNode
                tList.append(treenode.left)
            elif treenode.right is None:
                treenode.right = treeNode
                tList.append(treenode.right)
            else:
                tList.append(treenode.left)
                tList.append(treenode.right)
                insert_node(tList[p+1], p+1, treeNode)
                tList.append(self.root)
                insert_node(self.root, 0, treeNode)
# 广度优先遍历
def BFS(tree):
    tList = []
    def traverse(node, p):
        if node.right is not None:
            tList.append(node.right)
        if node.left is not None:
            tList.append(node.left)
        if p > (len(tList) - 2):
            return
        else:
            traverse(tList[p+1], p+1)
            tList.append(tree.root)
            traverse(tree.root, 0)
            for node in tList:
                print(node.data)
def DFS(tree):
    tList = []
    tList.append(tree.root)
    while len(tList) > 0:
        node = tList.pop()
        print(node.data)
        if node.right is not None:
            tList.append(node.right)
        if node.left is not None:
            tList.append(node.left)


TList = [1,2,3,4,5,6,7,9,8]
tree = BinaryTree()
for (i, j) in enumerate(TList):
    node = TreeNode(j, None, None)
    if i == 0:
        tree.make_tree(node)
    else:
        tree.insert(node)
print('深度优先遍历')
DFS(tree)
print('广度优先遍历')
BFS(tree)
