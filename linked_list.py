class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if(nodes is not None):
            node = Node(data=nodes.pop(0))
            self.head = node
            for i in nodes:
                node.next = Node(data=i)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


if __name__ == "__main__":
    linked_list = LinkedList(["a", "b", "c"])
    print(linked_list)