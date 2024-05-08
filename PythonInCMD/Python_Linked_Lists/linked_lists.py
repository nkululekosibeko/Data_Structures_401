class _Node:
    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None

    def printList(self):
        temp = self._head
        while (temp):
            print(temp._element)
            temp = temp._next

llist = LinkedList()
llist._head = _Node(1, None)
second = _Node(2, None)
third = _Node(3, None)

llist._head._next = second
second._next = third

print('Print Nodes')
llist.printList()