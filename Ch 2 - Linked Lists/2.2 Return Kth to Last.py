from LinkedList import Node, LinkedList


# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# assuming k < size of linked list
# "1 from last" is the second to last element, do not confuse terminology with absolute kth value from last
# "0 from last" would be the last element
def kthFromLast(n: Node, k: int):
    run = n

    for i in range(k):
        run = run.next

    while run.next:
        n = n.next
        run = run.next

    return n


ll = LinkedList([1, 2, 3, 4, 5])

print(kthFromLast(ll.getRoot(), 4))
print(kthFromLast(ll.getRoot(), 0))
print(kthFromLast(ll.getRoot(), 1))

# O(n) efficiency
# error handling for k > size would be trying the for loop and returning False if the loop goes out of range
# i.e. run being null before the for loop is complete
