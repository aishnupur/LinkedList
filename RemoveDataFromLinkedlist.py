class Node:
    # Create new node
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # Add element at the beginning
    def insertAtBeginning(self, data):
        newElement = Node(data)
        newElement.next = self.head
        self.head = newElement

    def popElementFromEnd(self):
        if self.head is None: 
            raise IndexError("Empty LinkedList, cannot pop")
        temp = self.head
        while temp.next and temp.next.next:
            temp = temp.next
        temp.next = None
        if temp == self.head:
            self.head = None

    def popElementFromBeginning(self):
        if self.head is None: 
            raise IndexError("Empty LinkedList, cannot pop")
        self.head = self.head.next
    
    # Print Elements in linked list
    def printElements(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

myLinkedList = LinkedList(4)
myLinkedList.insertAtBeginning(3)
myLinkedList.insertAtBeginning(5)
myLinkedList.insertAtBeginning(6)
print("Print the elements in the linkedlist: ")
myLinkedList.printElements()
print("Pop the element from the end ")
myLinkedList.popElementFromEnd()
print("Print the elements in the linkedlist: ")
myLinkedList.printElements()
print("Pop the element from the beginning ")
myLinkedList.popElementFromBeginning()
print("Print the elements in the linkedlist: ")
myLinkedList.printElements()
print("Pop the elements from an empty list ")
myLinkedList.popElementFromBeginning()
myLinkedList.popElementFromBeginning()
myLinkedList.popElementFromBeginning()

