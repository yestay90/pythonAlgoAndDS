
class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextNode = None

def cycle_check(node):

    couter = set()

    while node.nextNode != None:
        print("ceck loop")
        if node.value not in couter:
            couter.add(node.value)
        else :
            return True

        node = node.nextNode

    return False

a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c


value = cycle_check(a)
print(value)

