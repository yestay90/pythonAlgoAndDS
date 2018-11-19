
def isUniqueCharacters(s):

    char = set()

    for item in s:

        if item in char:
            return False
        else:
            char.add(item)

    return True

value = isUniqueCharacters('abbsert')
print(value)