
class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextNode = None


def nth_to_last_node(number, head):

    leftPointer = head
    rightPointer = head

    for i in range(number - 1):

        if not rightPointer.nextNode:
            raise  LookupError('ERror: n is larger that link list size')

        print('right point moved to ')

        rightPointer = rightPointer.nextNode
        print(rightPointer.value)

    while rightPointer.nextNode:

        leftPointer = leftPointer.nextNode
        rightPointer = rightPointer.nextNode

    return leftPointer



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e

value = nth_to_last_node(2, a)
#print(value.value)