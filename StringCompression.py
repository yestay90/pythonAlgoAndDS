
def compress(s):

    length = len(s)
    i = 1
    count = 1
    strtoreturn = s[i]

    while i < length:

        if s[i] == s[i - 1]:
            count += 1
        else:
            strtoreturn += str(count)
            strtoreturn += s[i]
            count = 1
        i+=1

    strtoreturn += str(count)

    return strtoreturn

value = compress('FFDDDNNNVVV')
print(value)