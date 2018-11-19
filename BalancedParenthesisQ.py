class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        length = len(self.items)
        return self.items[length - 1]

    def size(self):
        return len(self.items)


def balancedPa(s):

    stack = Stack()

    if len(s) % 2 != 0:
        return False

    openings = set('{[(')

    matches = set([('(', ')'), ('{', '}'), ('[', ']')])

    for item in s:

        if item in openings:
            stack.push(item)

        else:
            if stack.isEmpty():
                return False

            last_open = stack.pop()

            if (last_open,item) not in matches:
                return False

    return stack.isEmpty()

def balancedParentesis(s):

    stack = Stack()

    if len(s)%2 != 0:
        return False

    openings = set('{[(')

    i =  0

    while i <len(s):
        item = s[i]

        if  stack.isEmpty():
            if item not in openings:
                return False

        if (item == '[') or (item == '{') or (item == '('):
            print('push opening')
            stack.push(item)


        if item == "]":
            print("value swaured")
            if stack.peek() == "[":
                print('found squared')
                stack.pop()
            else:
                return False

        if item == "}":
            if stack.peek() == "{":
                stack.pop()
            else:
                return False

        if item == ")":
            if stack.peek() == "(":
                stack.pop()
            else:
                return False

        i += 1

    return stack.isEmpty()

value = balancedParentesis("{[]]]}")
print(value)

