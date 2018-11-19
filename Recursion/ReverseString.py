
def reverse(s):

    if len(s) <= 1:
        return s
    else:
        lastCharacter = s[-1]
        removedLastCharacterStr = s[:-1]
        reversedString = lastCharacter + reverse(removedLastCharacterStr)
        return reversedString

str = reverse("abc")
print(str)