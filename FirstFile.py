
def sum1(n):
    final_sum = 0

    for x in range(n + 1):
        final_sum += x

    return final_sum

value = sum1(10)
print(value)

def sum2(n):
    return (n*(n+1))/2

print(sum2(10))

def func_constant(values):
    print(values[0])

lst = [1,2,3,4,5]
func_constant(lst)

#list operation

def method1():
    l = []
    for n in range(1000):
        l = l + [n]

def method2():
    l = []
    for n in range(1000):
        l.append(n)