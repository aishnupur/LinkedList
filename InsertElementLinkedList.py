class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self, data, node):
        new_node = Node(data)
        if node is None:
            print("Does not exist")
        new_node.next = node.next
        node.next = new_node

if __name__ == '__main__':
    l = linkedlist()
    l.head = Node(1)
    m = Node(2)
    n = Node(3)
    l.head.next = m
    m.next = n
    print("Pushing element: ")
    l.push(7, m)
    l.push(9, m)
    l.print()
