
class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextNode = None


def reverseLinkedList(head):

    current =  head
    previous = None
    nextNode = None

    while current:

        nextNode = current.nextNode
        current.nextNode = previous

        previous = current
        current = nextNode

    return previous




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextNode = b
b.nextNode = c
c.nextNode = d

value = reverseLinkedList(a)
print(value.value)