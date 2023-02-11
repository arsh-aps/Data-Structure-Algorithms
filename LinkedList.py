class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def addToFront(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def addToMid(self, prevNode, value):
        if prevNode is None:
            print("Given previous node is not in the linked list.")
            return
        newNode = Node(value)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def addToEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = newNode

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = LinkedList()
llist.addToEnd(2)
llist.addToFront(1)
llist.addToEnd(3)
llist.addToMid(llist.head.next, 9)
llist.printLL()