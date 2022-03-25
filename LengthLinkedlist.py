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

    def length(self):
        count = 0
        temp = self.head
        while (temp):
            temp = temp.next
            count = count + 1
        print(count)


if __name__ == '__main__':
    l = linkedlist()
    l.head = Node(1)
    m = Node(6)
    n = Node(3)
    o = Node(9)
    l.head.next = m
    m.next = n
    n.next = o
    print("length is: ")
    l.length()
