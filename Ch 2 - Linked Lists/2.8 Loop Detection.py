from LinkedList import Node, LinkedList

# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C


# Method 1: using a dictionary
def loopDetection(n: Node):
    dict = {}

    while n:
        if n in dict:
            return n
        else:
            dict[n] = True
        n = n.next

    return None



ll = LinkedList([1,2,3,4,5])
loop = ll.get(3)
ll.append(loop)

print(loopDetection(ll.getRoot()))

# O(n) time and O(n) space


# Method 2: Runner technique, see Floyd's Tortoise and Hare algorithm at bottom of page
def loopDetectionRunner(n: Node):
    slow = n
    fast = n

    # Find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # loop found, searching for start point
        if slow == fast:
            slow = n
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None


print(loopDetectionRunner(ll.getRoot()))

# O(n) time and O(1) space, so method 2 is recommended

# Floyd's Tortoise and Hare algorithm is used to detect circular loops

# Here's how the algorithm works:
# 1) Initialize two pointers, slow (tortoise) and fast (hare), both at the beginning of the linked list.
# 2) Move the slow pointer one step at a time (slow = slow.next), and move the fast pointer two steps at a time
# (fast = fast.next.next).
# 3) If the linked list contains a loop, the fast pointer will eventually catch up to the slow pointer, and they will
# meet at a common node within the loop. If there's no loop, the fast pointer will reach the end of the linked list
# (fast == None).
# this is usually where the algorithm stops, as it is set up to detect if a linked list is circular,
# extra steps are implemented in this exercise to find the beginning of the loop, which are as follows:
# 4) Once the slow and fast pointers meet, reset the slow pointer to the beginning of the linked list.
# 5) Move both the slow and fast pointers one step at a time. They will meet again at the node where the loop starts.
# This is the point of intersection.
