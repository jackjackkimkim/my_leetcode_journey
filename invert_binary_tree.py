from typing import List
from typing import Optional


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)


def printtree(root):

    if root == None:
        return
    # First print the data of node
    print(root.data, end=": ")
    # if root.left != None:
    #     print(root.left, end=": ")
    # if root.right != None:
    #     print(root.right, end=": ")

    print()
    # Then recur on left child
    printtree(root.left)

    # Finally recur on right child
    printtree(root.right)


root1 = Node(4)
root2 = Node(2)
root3 = Node(7)
root4 = Node(1)
root5 = Node(3)
root6 = Node(6)
root7 = Node(9)

root1.left = root2
root1.right = root3
root2.left = root4
root2.right = root5
root3.left = root6
root3.right = root7

printtree(root1)


class Solution:
    def invertTree(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
