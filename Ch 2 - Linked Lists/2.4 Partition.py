from LinkedList import Node, LinkedList


# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:
# Output:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

def partitionList(n: Node, partition: int):
    # Setting up left and right lists, giving them dummy values that will be removed later,
    # This is done so that the program doesn't need to check if the lists are None every operation in the while loop.
    left, right = Node(None), Node(None)
    leftHead, rightHead = left, right


    while n:
        t = Node(n.value)

        if n.value < partition:
            left.next = t
            left = t
        else:
            right.next = t
            right = t

        n = n.next

    print(leftHead.next)

    leftHead = leftHead.next
    rightHead = rightHead.next

    left.next = rightHead

    # returns a new linked list instead of just the head node
    return LinkedList(leftHead)


ll = LinkedList([3, 5, 8, 5, 10, 2, 1])
print(ll)
partitionList(ll.getRoot(), 5)
print(partitionList(ll.getRoot(), 5))

# O(n) time complexity, going through each element in the linked list
# Output varies BUT fulfills the criteria
