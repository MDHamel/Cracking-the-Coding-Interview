from LinkedList import Node, LinkedList

# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter
# secting node. Note that the intersection is defined based on reference, not value.That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.


def intersection(a: Node, b: Node):
    dict = {}

    while a:
        dict[a] = True
        a = a.next

    while b:
        if b in dict:
            return b
        b = b.next

    return None



# O(n) time complexity, but it does use a space complexity of O(n) as well, however, it can be reduced to O(1) space if
# the dictionary were removed