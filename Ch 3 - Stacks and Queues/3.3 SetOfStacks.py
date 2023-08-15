from StackAndQueue import Stack, Node


# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.

class SetOfStacks:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currentStackCount = 0
        self.stacks = Stack(Stack())

    def push(self, val):
        currentStack = self.stacks.peek()

        currentStack.push(val)
        self.currentStackCount += 1

        if self.currentStackCount == self.capacity:
            self.stacks.push(Stack())
            self.currentStackCount = 0

    def pop(self):
        currentStack = self.stacks.peek()

        if currentStack.isEmpty():
            self.stacks.pop()
            currentStack = self.stacks.peek()

        return currentStack.pop() if not currentStack.isEmpty() else False    # current stack is empty, stacks is empty

    def peek(self):
        return self.stacks.peek().peek()

# Follow up: Given popAt(int index), use an array instead of a stack, that way you can get the corresponding index by
# doing: stackIndex = index//capacity and then have the stack pop index%capacity times into a temporary stack, pop
# the item, and then refill the stack

