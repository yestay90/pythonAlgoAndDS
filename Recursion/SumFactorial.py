
def Sum(n):

    if n == 0:
        return 0

    return n + Sum(n - 1)

value = Sum(4)
# print(value)

# 4592
def sum2(n):

    if n  < 10:
        return  n

    return  int(round(n%10)) + sum2(n/10)

value2 = sum2(4321)
print(value2)

