
"""
二叉搜索树
"""

class Node(object):
    def __init__(self,value, left, right,parent):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class BST(object):
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        pass

    def search(self, value):
        pass

    def delete(self, value):
        pass

    def update(self, value):
        pass

    def prev_travce(self):
        pass


bst = BST(10)
bst.insert(1)
bst.prev_travce()