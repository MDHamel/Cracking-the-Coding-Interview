from LinkedList import Node, LinkedList

# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.


# method 1, brute force
def sumList(a: Node, b: Node):
    numA = 0
    numB = 0

    mult = 1  # multiple

    while a:
        numA += a.value * mult

        mult *= 10
        a = a.next

    mult = 1

    while b:
        numB += b.value * mult

        mult *= 10
        b = b.next

    s = numA + numB
    n = Node(-1)  # dummy node, removed at return
    nHead = n

    while s > 0:
        n.next = Node(s % 10)
        n = n.next
        s //= 10

    return nHead.next


# Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
ll1 = LinkedList([7, 1, 6])
ll2 = LinkedList([5, 9, 2])

summed = LinkedList(sumList(ll1.getRoot(), ll2.getRoot()))
print(summed)


# method 2, a different implementation
def sumList2(a, b):
    n = Node(0)     # node root has value of one, which exists, so it adds the value of a+b
    nHead = n       # head to return

    while a or b:
        aval = a.value if a else 0
        bval = b.value if b else 0
        value = aval + bval

        if n:
            n.value += value
        else:
            n = Node(value)

        if n.value > 9:
            carryOver = n.value // 10
            n.value %= 10
            n.next = Node(carryOver)

        n = n.next
        a = a.next
        b = b.next

    return nHead


summed = LinkedList(sumList2(ll1.getRoot(), ll2.getRoot()))
print(summed)

# Method 2 is more efficient in practice, but both have O(n) time,
# however, since method 2 uses fewer operations, it is considered more efficient at a low level

# =================================================================================================================== #
# =================================================================================================================== #


# Forwards implementation, we can't use method 2 since we don't know if the numbers have the same rank, as a result we
# could add the 100's place to the 10's place, for example
def sumListForwards(a, b):
    n = Node(0)     # dummy root
    nHead = n       # head to return

    values = []

    while a or b:
        numa = a.value if a else 0
        numb = b.value if b else 0

        values.append(numa+numb)

        a = a.next
        b = b.next

    for v in values:
        n.next = Node(v % 10)
        if v > 9:
            n.value += 1
        n = n.next

    return nHead.next

# Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

ll1 = LinkedList([6, 1, 7])
ll2 = LinkedList([2, 9, 5])

summed = LinkedList(sumListForwards(ll1.getRoot(), ll2.getRoot()))
print(summed)

#All implementations are O(n) where n is the longest length of linked lists a and b