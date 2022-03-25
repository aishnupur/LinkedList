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

    def nthnode(self, n):
        temp = self.head
        while temp:
            if temp == n:
                print(temp.data)
                break
            temp = temp.next

if __name__ == '__main__':
    l = linkedlist()
    l.head = Node(1)
    m = Node(2)
    n = Node(3)
    l.head.next = m
    m.next = n
    print("Search nth node: ")
    l.nthnode(m)

