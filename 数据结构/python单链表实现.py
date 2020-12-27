class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node(0)

    def get(self, index: int) -> int:
        if index < 0: return -1
        node = self.head
        for _ in range(index + 1):
            if node.next is not None:
                node = node.next
            else:
                return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        self.head.next = new

    def addAtTail(self, val: int) -> None:
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head
        for i in range(index):
            if node is None:
                return
            node = node.next
        if node is None:
            node = Node(val)
        else:
            new = Node(val)
            new.next = node.next
            node.next = new

    def deleteAtIndex(self, index: int) -> None:
        if index < 0: return
        node = self.head
        for _ in range(index):
            node = node.next
        if node.next is not None:
            node.next = node.next.next

