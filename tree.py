class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if(node):
            self.root = node
        elif(data):
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if(node is None):
            node = self.root
        if(node.left):
            self.simetric_traversal(node.left)
        print(node)
        if(node.right):
            self.simetric_traversal(node.right)


if(__name__ == "__main__"):
    tree = BinaryTree()
    n1 = Node(10)
    n2 = Node(5)
    n3 = Node(100)
    n4 = Node(2)
    n5 = Node(17)
    n6 = Node(9)
    n7 = Node(52)

    n5.right = n7
    n5.left = n6
    n2.right = n4
    n2.left = n3
    n1.right = n5
    n1.left = n2

    tree.root = n1
    print(tree.simetric_traversal())