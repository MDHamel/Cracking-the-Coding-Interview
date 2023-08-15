from StackAndQueue import Stack, Node


# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty

class SortedStack:
    def __init__(self):
        self.stack = Stack()

    def peek(self):
        return self.stack.peek()

    def push(self, item):
        retainer = Stack()

        while not self.stack.isEmpty() and self.stack.peek().value < item:
            retainer.push(self.stack.pop().value)

        self.stack.push(item)

        while not retainer.isEmpty():
            self.stack.push(retainer.pop().value)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack.isEmpty()

    def __str__(self):
        return str(self.stack)


s = SortedStack()
s.push(3)
s.push(5)
s.push(4)
s.push(1)
s.push(2)

print(s)
print("Popping", s.pop())
print(s)