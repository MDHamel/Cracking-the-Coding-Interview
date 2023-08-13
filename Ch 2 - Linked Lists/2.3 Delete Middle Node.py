from LinkedList import Node, LinkedList


# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.


def deleteMiddle(n: Node):
    run = n.next.next

    while run and run.next:
        run = run.next.next if run.next and run.next.next else run.next

        n = n.next

    n.next = n.next.next


ll = LinkedList([1, 2, 3, 4, 5])
deleteMiddle(ll.getRoot())
print(ll)

ll = LinkedList([1, 2, 3,])
deleteMiddle(ll.getRoot())
print(ll)

ll = LinkedList([1, 2, 3, 4])
deleteMiddle(ll.getRoot())
print(ll)

# O(n) time complexity, goes through each element to get to the middle of the list.
# Note that this is the best provided, sending over the size would still preform n operations
# remember that O(n/2) is still O(n), there are different methods in which splitting the problem increases efficiency,
# but not here. n in this case would be half the size of the list for both instances
