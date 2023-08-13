from LinkedList import LinkedList, Node


def removeDups(n: Node):
    cur = n

    while cur:
        runner = cur
        while runner.next:
            if runner.next.value == cur.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next


ll = LinkedList([1,2,3,4,3,5])

removeDups(ll.getRoot())
print(ll)

# without buffer, O(n^2), a buffer would increase space complexity but reduce time complexity to O(n) if done with a
# dictionary or similar structure
