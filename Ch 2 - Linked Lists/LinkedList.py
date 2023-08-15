class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "( {0} )".format(self.value)


class DoublyNode(Node):
    def setPrevious(self, prevNode):
        self.prev = prevNode


# wrappers
class LinkedList:
    def __init__(self, root: Node | None | list = None):
        self.size = 1 if root else 0
        if isinstance(root, Node | None):
            self.root = root
            self.tail = root
        elif isinstance(root, list):
            self.tail = None
            self.appendValues(root)

    # append new value to end of list
    def append(self, val):
        if isinstance(val, list):
            self.appendValues(val)
            return

        newNode = val if isinstance(val, Node) else Node(val)

        if self.root:
            n = newNode
            self.tail.next = n
            self.tail = n
        else:
            self.root = newNode
            self.tail = self.root

        self.size += 1

    # append a list of values to the linked list
    def appendValues(self, values: list):
        cur = None

        if self.tail:
            cur = self.tail
        else:
            cur = Node(values.pop(0))
            self.root = cur

        for v in values:
            n = Node(v)
            cur.next = n
            cur = n
        self.tail = cur
        self.size += len(values)

    # insert at a certain index, returns False if not index is out of range
    def insert(self, val, index: int):

        if index >= self.size:
            return False

        cur = self.root

        for i in range(index):
            cur = cur.next

        temp = cur.next
        n = Node(val)
        cur.next = n
        n.next = temp
        self.size += 1

    # remove first instance of value, if removed returns true
    def remove(self, val):

        if self.size == 0:
            return False

        cur = self.root
        prev = None

        while cur:
            if cur.value == val:
                if prev:
                    prev.next = cur.next

                del cur
                self.size -= 1
                return True
            prev = cur
            cur = cur.next

        return False

    # remove at a certain index, if removed returns true
    def removeAt(self, index: int):

        if self.size == 0:
            return False

        cur = self.root

        for i in range(index):
            temp = cur.next
            cur.next = cur.next.next
            del temp
            self.size -= 1
            return True

        return False

    def get(self, index: int):
        n = self.root

        for _ in range(index):
            n = n.next

        return n

    def __contains__(self, item):
        cur = self.root

        while cur:
            if cur.value == item:
                return True
            cur = cur.next

        return False

    def getRoot(self):
        return self.root

    def __len__(self):
        return self.size

    def __str__(self):
        cur = self.root
        values = []

        while cur:
            values.append("( {0} )".format(str(cur.value)))
            cur = cur.next

        return " -> ".join(values)


