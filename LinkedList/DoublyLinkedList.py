
class DoublyLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.prev_node = None
        self.next_node = None


a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b
