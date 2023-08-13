class Node:
    # Create new node
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    # Append the element at the end
    def insertAtEnd(self, data):
        newElement = Node(data)
        if self.head is None: 
            self.head = newElement
            return
        dummy = self.head
        while dummy.next:
            dummy = dummy.next
        dummy.next = newElement

    # Add element at the beginning
    def insertAtBeginning(self, data):
        newElement = Node(data)
        newElement.next = self.head
        self.head = newElement

    # Add element in the middle of the linkedlist
    def insertElementInMiddle(self, index, data):
        if index == 0:
            self.insertAtBeginning(data)
            return

        newElement = Node(data)
        temp = self.head
        for _ in range(index - 1):
            if temp is None:
                raise IndexError("Index out of range")
            temp = temp.next

        newElement.next = temp.next
        temp.next = newElement
    
    # Print Elements in linked list
    def printElements(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

myLinkedList = LinkedList(4)
myLinkedList.insertAtEnd(5)
myLinkedList.insertAtBeginning(3)
myLinkedList.insertAtBeginning(6)
myLinkedList.insertElementInMiddle(3,8)
myLinkedList.printElements()