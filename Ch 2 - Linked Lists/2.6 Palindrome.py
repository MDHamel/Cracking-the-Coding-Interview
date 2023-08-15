from LinkedList import Node, LinkedList


# Palindrome: Implement a function to check if a linked list is a palindrome.

# Method uses a singly node and only given the head. Tried not to use additional data structures, as it didnt seem
# necessary
def palindromeCheck(n: Node):
    nhead = n
    rev = Node(n.value)

    n = n.next
    while n:
        temp = Node(n.value)
        temp.next = rev
        n = n.next
        rev = temp

    while nhead:
        if nhead.value != rev.value:
            return False

        rev = rev.next
        nhead = nhead.next

    return True


# should be true
ll = LinkedList([1, 2, 3, 2, 1])
print(palindromeCheck(ll.getRoot()))

# should be false
ll = LinkedList([1, 2, 3, 1])
print(palindromeCheck(ll.getRoot()))

# should be true
ll = LinkedList([1, 2, 2, 1])
print(palindromeCheck(ll.getRoot()))

# O(n) complexity, it does go through the list twice, to find the end, and then it goes back from comparing each value.
# would be faster if given a doubly linked list and having the parameters take the head and tail, but for a singly list
# this is the most efficient use of time and space

