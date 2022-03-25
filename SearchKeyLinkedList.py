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

    def search(self, key):
        count = 0
        temp = self.head
        while (temp):
            if temp.data == key:
                return True
            temp = temp.next
            count = count + 1
        return False


if __name__ == '__main__':
    l = linkedlist()
    l.head = Node(1)
    m = Node(6)
    n = Node(4)
    l.head.next = m
    m.next = n
    print("Search element: ")
    print(l.search(6))
