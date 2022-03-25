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


    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == '__main__':
    l = linkedlist()
    l.head = Node(1)
    m = Node(2)
    n = Node(3)
    l.head.next = m
    m.next = n
    print("Reverse the linkedlist: ")
    l.reverse()
    l.print()