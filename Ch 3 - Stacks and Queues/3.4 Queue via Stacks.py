from StackAndQueue import Stack, Node


# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:
    def __init__(self):
        self.stack = Stack()


    def push(self, val):
        s1 = self.stack
        s2 = Stack()
        while not s1.isEmpty():
            s2.push(s1.pop().value)

        s1.push(val)

        while not s2.isEmpty():
            s1.push(s2.pop().value)

        self.stack = s1


    def peek(self):
        return self.stack.peek()

    def remove(self):
        return self.stack.pop()

    def isEmpty(self):
        print(self.stack)
        return self.stack.isEmpty()

    def __str__(self):
        return str(self.stack)


q = MyQueue()

q.push(1)
q.push(2)
q.push(3)

print(q)

print("Removing: ", q.remove())

print(q)
