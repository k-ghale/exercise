
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtBeginning(head, x):
    newNode = Node(x)
    newNode.next = head
    return newNode

def printList(head):
    current = head
    while(current):
        print(current.data)
        current = current.next

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

head = insertAtBeginning(head, 60)

printList(head)

