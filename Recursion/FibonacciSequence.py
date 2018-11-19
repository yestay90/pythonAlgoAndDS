
def findNThelementOfFib(n):

    #base case
    if n == 0 or n == 1:
        return n
    else:
        return findNThelementOfFib(n - 2) + findNThelementOfFib(n - 1)

value = findNThelementOfFib(6)
# print(value)

def fib_iteratevely(n):

    a = 0
    b = 1

    for i in range(n):
        a,b = b, a + b

    return a

value2 = fib_iteratevely(10)


n = 10
cache = [None] * (n+1)

def fib_dyn(n):
    #base case
    if n == 0 or n == 1:
        return n

    #check cache
    if cache[n] != None:
         return cache[n]

    #set cache
    cache[n] = fib_dyn(n -1) + fib_dyn(n -2)

    return cache[n]