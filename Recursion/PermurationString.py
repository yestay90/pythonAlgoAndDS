def permute(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        #for every letter in string
        for i,let in enumerate(s):
            #from every permutation resulting from step 2 and step 3
            print('s[:i] is ', s[:i])
            print('s[i + 1:] is', s[i + 1])
            for perm in permute(s[:i] + s[i + 1:]):

                print('letter is', let)
                print('perm is ', perm)

                out += [let + perm]


    return out

value = permute("abc")

print(value)


