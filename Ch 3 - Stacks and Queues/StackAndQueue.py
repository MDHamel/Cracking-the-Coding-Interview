class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "[ {0} ]".format(self.value)


# A stack is a link list where the first item is the only item in the stack that doesn't have a next and goes backwards,
# instead of assigning the next node, you assign the current one to a new previous node
class Stack:
    def __init__(self, item = None):
        self.top = None
        if isinstance(item, Node):
            self.top = item
        elif isinstance(item, list):
            self.push(item)
        elif item:
            self.top = Node(item)

    # returns value if there is one, otherwise returns false. Reminder: pop's the node, not the value
    def pop(self):
        if self.isEmpty():
            return False

        temp = self.top
        self.top = self.top.next
        return temp

    def peek(self):
        return self.top

    def push(self, item):
        temp = None
        if isinstance(item, Node):
            temp = item
        elif isinstance(item, list):  # if the push item is a list, push each item. Can't be a stack of arrays
            for i in item:
                self.push(i)
            return
        elif item:
            temp = Node(item)

        if self.top and temp:
            temp.next = self.top

        self.top = temp

    #
    def isEmpty(self):
        return self.top is None

    def __str__(self):
        values = []
        cur = self.top
        while cur:
            values.append(str(cur))
            cur = cur.next

        return "\n".join(values)

